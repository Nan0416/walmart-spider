from scrapying_scripts.spiders.walmart_product_spider import WalmartProductSpider

class WalmartToyCategory(WalmartProductSpider):
    def __init__(self):
        super().__init__()
        self.category = 'toy'

class WalmartRCCarSpider(WalmartToyCategory):
    name = "walmart-radio-control-car"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/search/?cat_id=4171_1111647&page=%d'
        self.product_type = "radio-control-car"

class WalmartDollsSpider(WalmartToyCategory):
    name = "walmart-dolls"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/dolls-dollhouses/fashion-dolls/4171_4187_133047?page=%d'
        self.product_type = "dolls"
