from datetime import datetime


class Ticket:

    def __init__(self, root_number: int, price_ticket: float = None, place: int = None, date_time: datetime = datetime.now()):
        self.root_number = root_number
        self.price_ticket = price_ticket
        self.place = place
        self.date_time = date_time
        self.is_valid: bool = False

    def __str__(self):
        return f'Ticket №{self.root_number} paid = {self.is_valid}'

