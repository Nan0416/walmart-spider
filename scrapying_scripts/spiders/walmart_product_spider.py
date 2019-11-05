import scrapy
import json
from scrapying_scripts.items import Product, FailedItem

class WalmartProductSpider(scrapy.Spider):
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.product_pages = 25
        self.base_url = ""
        self.product_type = ""
        self.category = ""
        self.filename = type(self).name
        self.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36"
        }

    def start_requests(self):
        for id in range(1, self.product_pages + 1):
            yield scrapy.Request(
                url = self.base_url % id,
                callback = self.parse_metalink,
                method = 'GET',
                headers = self.headers
            )

    def parse_metalink(self, response):
        prefix_str = '<script id="searchContent" type="application/json">'
        suffix_str = '</script>'
        data = response.css('#searchContent').get() 
        data = data[len(prefix_str): -1 * len(suffix_str)]
        data = json.loads(data)
        items = data['searchContent']['preso']['items']
        for item in items:
            url = 'https://www.walmart.com' + item['productPageUrl']
            yield scrapy.Request(
                url = url, 
                callback=self.parse_product,
                method = 'GET',
                headers = self.headers
            )

    def parse_product(self, response):
        # print(dir(response))
        prefix_str = '<script id="item" type="application/json">'
        suffix_str = '</script>'
        data = response.css('#item').get()
        if data is None:
            return
        data = data[len(prefix_str): -1 * len(suffix_str)]
        data = json.loads(data)
        try:
            yield self.json_to_item(data, response.request.url)
        except Exception as ex:
            yield FailedItem(
                url = response.request.url,
                reason = str(ex)
            )

    def json_to_item(self, data, product_url):
        pid = data['item']['product']['buyBox']['primaryProductId']
        product = data['item']['product']['buyBox']['products'][0]
        image_urls = []
        for img in product['images']:
            image_urls.append(img['url'])
        review_num = 0
        rating = 0
        review = data['item']['product']['reviews'].get(pid)
        if review is not None:
            review_num = review.get('totalReviewCount')
            rating = review.get('roundedAverageOverallRating')
        return Product(
            url = product_url,
            category = self.product_type,
            id = pid, 
            name = product['productName'],
            image_urls = image_urls,
            price = product['priceMap']['price'],
            brand = product['brandName'],
            review_num = review_num if review_num is not None else 0,
            rating = rating if rating is not None else 0,
            department = self.category
            )

    def tofile(self, filename, data):
            with open(filename, 'w') as f:
                f.write(json.dumps(data, sort_keys=True, indent=4))