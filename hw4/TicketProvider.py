from Ticket import Ticket


class TicketProvider:
    count_id = 0
    ticket_list: dict = {}

    def create_ticket(self) -> Ticket:
        self.count_id += 1
        ticket = Ticket(self.count_id)
        self.ticket_list[ticket.root_number] = ticket
        return ticket

    def update_ticket(self, ticket: Ticket) -> bool:
        ticket.is_valid = True
        return True

    def get_ticket(self, root_number: int) -> Ticket:
        return self.ticket_list[root_number]
