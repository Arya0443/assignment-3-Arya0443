class Home:
    __slots__ = ["garden", "indoor", "bathroom", "total_price"]
    def __init__(self, garden, indoor, bathroom, total_price):
        self.garden = garden
        self.indoor = indoor
        self.bathroom = bathroom
        self.total_price = total_price
