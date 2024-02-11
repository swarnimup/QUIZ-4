from dataclasses import dataclass

@dataclass
class MyDataClass:
    name: str
    price: float
    quantity: int = 0
