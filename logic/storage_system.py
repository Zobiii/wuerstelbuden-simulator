from datetime import date, timedelta


class StorageSystem:
    def __init__(self):
        self.today = date.today()
        self.items = {
            "Würstel": [],
            "Semmeln": [],
            "Senf": [],
        }

    def add_item(self, name, quantity, shelf_life_days):
        expiry = self.today + timedelta(days=shelf_life_days)
        for _ in range(quantity):
            self.items[name].append(expiry)

    def remove_expired_items(self):
        for name in self.items:
            self.items[name] = [exp for exp in self.items[name] if exp > self.today]

    def advance_day(self):
        self.today += timedelta(days=1)
        self.remove_expired_items()

    def get_inventory(self):
        summary = {}
        for name, dates in self.items.items():
            counts = {}
            for exp in dates:
                if exp in counts:
                    counts[exp] += 1
                else:
                    counts[exp] = 1
            summary[name] = counts
        return summary
