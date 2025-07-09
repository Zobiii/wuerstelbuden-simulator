class Economy:
    def __init__(self, starting_money=100.0):
        self.balance = starting_money

    def get_balance(self):
        return round(self.balance, 2)

    def spend(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def earn(self, amount):
        self.balance += amount
