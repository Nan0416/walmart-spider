from scrapying_scripts.spiders.walmart_product_spider import WalmartProductSpider

class WalmartFurnitureCategory(WalmartProductSpider):
    def __init__(self):
        super().__init__()
        self.category = 'furniture'

class WalmartBedSpider(WalmartFurnitureCategory):
    name = "walmart-bed"
    def __init__(self):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/bedroom-furniture/beds/4044_103150_102547_91837?page=%d'
        self.product_type = "bed"

class WalmartDiningRoomSetSpider(WalmartFurnitureCategory):
    name = "walmart-dining-room-set"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/4044_103150_4037_3500031?page=%d'
        self.product_type = "dining-room-set"

class WalmartDeskSpider(WalmartFurnitureCategory):
    name = "walmart-desk"
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.product_pages = 25
        self.base_url = 'https://www.walmart.com/browse/office-furniture/desks/4044_103150_97116_91851?page=%d'
        self.product_type = 'desk'