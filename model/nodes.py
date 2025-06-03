import datetime
from dataclasses import dataclass

@dataclass
class Node:
    order_id: int
    customer_id: int
    order_status: int
    order_date: datetime.datetime
    required_date: datetime.datetime
    shipped_date: datetime.datetime
    store_id: int
    staff_id: int

    def __hash__(self):
        return self.order_id
