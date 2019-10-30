from scrapying_scripts.spiders.walmart_product_spider import WalmartProductSpider

class WalmartElectronicsCategory(WalmartProductSpider):
    def __init__(self):
        super().__init__()
        self.category = 'electronics'


class WalmartTVSpider(WalmartElectronicsCategory):
    name = "walmart-tv"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/electronics/tvs/3944_1060825_447913?page=%d'
        self.product_type = "tablet"
        self.filename = WalmartTVSpider.name

class WalmartLaptopSpider(WalmartElectronicsCategory):
    name = "walmart-laptop"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/electronics/all-laptop-computers/3944_3951_1089430_132960?page=%d'
        self.product_type = "laptop"
        self.filename = WalmartLaptopSpider.name

class WalmartTabletSpider(WalmartElectronicsCategory):
    name = "walmart-tablet"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = "https://www.walmart.com/browse/ipad-tablets/tablet-pcs/3944_1078524_1078084?page=%d"
        self.product_type = "tablet"
    
class WalmartCellPhoneSpider(WalmartElectronicsCategory):
    name = 'walmart-cellphone'
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/search/?cat_id=1105910_2538833&page=%d'
        self.product_type = 'cellphone'