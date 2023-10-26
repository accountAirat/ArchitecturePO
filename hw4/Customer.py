import TicketProvider, Ticket, CashProvider
from typing import List

from datetime import datetime


class Customer:

    def __init__(self, cash_provider: CashProvider, ticket_provider: TicketProvider, pk: int = None):
        self.pk = pk
        self.tickets = []
        self.cash = cash_provider
        self.ticket_provider = ticket_provider

    # Контракт
    def buy_ticket(self, ticket: Ticket) -> bool:
        if self.cash.buy(ticket):
            return self.ticket_provider.update_ticket(ticket)
        return False

    def search_ticket(self, date_time: datetime) -> List[Ticket]:
        return [i for i in self.tickets if i.date_time == date_time]

    def __str__(self):
        return f'Customer №{self.pk}'
