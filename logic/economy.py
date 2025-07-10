import math


class Economy:
    def __init__(self, starting_money=100.0):
        self.balance = starting_money
        self.debt = 0.0

    def get_balance(self):
        return round(self.balance, 2)

    def spend(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def earn(self, amount):
        self.balance += amount

    def take_loan(self, amount):
        self.balance += amount
        self.debt += amount
        return amount

    def get_debt(self):
        return round(self.debt, 2)
