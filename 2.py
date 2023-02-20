from dataclasses import dataclass, field


class LenEqualStr(str):
    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (str, LenEqualStr)):
            raise TypeError("class type can be only str or LenEqualStr")
        print('here')
        return len(self) == len(other)


@dataclass(slots=True)
class Technic():
    name: LenEqualStr
    price: int
    exist: bool
    # category: str = field(init=False)
    # expensive_price_separator: int = field(init=False, default=1000)

    # def __post_init__(self):
    #     self.category = "expensive" if self.price > self.expensive_price_separator else "cheep"


a = Technic(LenEqualStr('qwer'), 13, True)
b = Technic(LenEqualStr('hjkl'), 13, False)
print(a.name == b.name)


