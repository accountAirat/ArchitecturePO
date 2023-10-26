from Customer import Customer
from CashProvider import CashProvider
from TicketProvider import TicketProvider

from random import randint

customers = []
for i in range(1, 100):
    customer = Customer(cash_provider=CashProvider(randint(100_000, 999_999)),
                        ticket_provider=TicketProvider(),
                        pk=i)
    for j in range(10):
        ticket = customer.ticket_provider.create_ticket()
        if j % 2:
            customer.buy_ticket(ticket)
        customer.tickets.append(ticket)
    customers.append(customer)

for i in customers:
    print(i)
    for j in i.tickets:
        print(j)
    print()

