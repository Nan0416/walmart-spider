from scrapying_scripts.spiders.walmart_product_spider import WalmartProductSpider

class WalmartClothingCategory(WalmartProductSpider):
    def __init__(self):
        super().__init__()
        self.category = 'clothing'

class WalmartMensSweaterSpider(WalmartClothingCategory):
    name = "walmart-mens-sweaters"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 21
        self.base_url = 'https://www.walmart.com/search/?cat_id=5438_133197_5281276&page=%d'
        self.product_type = "mens-sweaters"


class WalmartMensJeansSpider(WalmartClothingCategory):
    name = "walmart-mens-jeans"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 21
        self.base_url = 'https://www.walmart.com/browse/clothing/jeans/5438_133197_6127105?page=%d'
        self.product_type = "mens-jeans"

class WalmartWomensJeansSpider(WalmartClothingCategory):
    name = "walmart-womens-jeans"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 21
        self.base_url = 'https://www.walmart.com/browse/clothing/women/5438_133162?cat_id=5438_133162_3193312&page=%d'
        self.product_type = "womens-jeans"
