class Home:
    __slots__ = ["garden", "indoor", "bathroom", "total_price"]
    def __init__(self, garden, indoor, bathroom, total_price):
        self.garden = garden
        self.indoor = indoor
        self.bathroom = bathroom
        self.total_price = total_price

class Home_Category:
    __slots__ = ["name", "code", "price", "category"]
    def __init__(self, name, code, price, category):
        self.name = name
        self.code = code
        self.price = price
        self.category = category
