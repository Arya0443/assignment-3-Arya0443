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

home = Home([],[],[],50.0)
garden_items = {"p": ("3 Pack garden flower", 5.0), "l": ("Hanging light wire", 10.0), "b": ("Garden bench", 35.0)}
indoor_items = {"t": ("Small table lamp", 5.0), "f1": ("City picture frame", 7.0), "r": ("Entry rug", 35.0), "f2": ("Flower vase", 14.0)}
bathroom_items = {"m": ("Wall mirror", 15.0), "c": ("Shower curtains", 10.0), "w": ("Wall mount", 7.0)}
