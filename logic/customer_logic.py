import random


class CustomerLogic:
    def __init__(self):
        pass

    def simulate_day(self, weather, prices):
        base_customer = {
            "Sonne": 30,
            "Bewölkt": 20,
            "Regen": 10,
            "Sturm": 5,
            "Heiß": 25,
            "Kalt": 15,
        }

        num_customer = base_customer.get(weather, 20)

        price_modifier = sum(prices.values()) / len(prices)

        if price_modifier > 3.0:
            num_customer *= 0.6
        elif price_modifier < 1.5:
            num_customer *= 1.2

        num_customer = int(num_customer)

        purchases = []

        for _ in range(num_customer):
            choice = random.choices(
                ["Würstel", "Semmeln", "Senf", None], weights=[0.5, 0.3, 0.1, 0.1]
            )[0]
            if choice:
                purchases.append(choice)

        return purchases
