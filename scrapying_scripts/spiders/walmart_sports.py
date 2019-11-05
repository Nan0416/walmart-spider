from scrapying_scripts.spiders.walmart_product_spider import WalmartProductSpider

class WalmartSportsCategory(WalmartProductSpider):
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.category = 'sports'

class WalmartSportsSpider(WalmartSportsCategory):
    name = "walmart-sports"
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/search/?cat_id=4125_4161&page=%d'
        self.product_type = "sports"