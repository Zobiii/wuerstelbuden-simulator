import logging


class Economy:
    def __init__(self, starting_money=100.0):
        self.balance = starting_money
        self.debt = 0.0

    def get_balance(self):
        return round(self.balance, 2)

    def spend(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            logging.info(f"Geld ausgegeben: {amount:.2f}")
            return True
        return False

    def earn(self, amount):
        self.balance += amount
        logging.info(f"Geld eingenommen: {amount:.2f}")

    def take_loan(self, amount):
        self.balance += amount
        self.debt += amount
        logging.info(f"Kredit aufgenommen: {amount:.2f}")
        return amount

    def get_debt(self):
        return round(self.debt, 2)
