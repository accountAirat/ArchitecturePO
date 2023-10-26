import Customer


class CashProvider:
    def __init__(self, card: int):
        self.card = card
        self.is_autorization = False

    def buy(self, price: int) -> bool:
        return True

    def autorization(self, customer: Customer) -> bool:
        return True
