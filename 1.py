from dataclasses import dataclass, field


@dataclass(slots=True)
class Technic():
    name: str
    price: int
    exist: bool
    category: str = field(init=False)
    expensive_price_separator: int = field(init=False, default=1000)
    
    def __post_init__(self):
        self.category = "expensive" if self.price > self.expensive_price_separator else "cheep"
