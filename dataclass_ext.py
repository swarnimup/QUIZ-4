from dataclasses import dataclass

@dataclass
class MyExtendedDataClass:
    name: str
    price: float
    quantity: int = 0

    def write_your_own_function(self):
        # Your meaningful function code here
        pass
