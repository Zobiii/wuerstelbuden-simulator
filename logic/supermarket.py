import random


class Supermarket:
    BASE_PRICES = {
        "Würstel": 1.50,
        "Semmeln": 0.50,
        "Senf": 0.30,
    }

    def __init__(self):
        self.prices = {}
        self.generate_new_prices()

    def generate_new_prices(self):
        for item, base in self.BASE_PRICES.items():
            deviation = base * random.uniform(-0.1, 0.1)
            self.prices[item] = round(base + deviation, 2)

    def get_prices(self):
        return self.prices.copy()
