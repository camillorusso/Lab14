import datetime
from dataclasses import dataclass

@dataclass
class Edge:
    order_id1: int
    order_id2: int
    peso: int
    verso: int