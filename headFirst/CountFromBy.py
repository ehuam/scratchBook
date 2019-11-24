class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.__val = v
        self.__incr = i

    def increase(self) -> None:
        self.__val += self.__incr

#    def __str__(self) -> str:
#       return str(self.__val)

    @property
    def val(self):
        print("Getting Value")
        return self.__val

    @val.setter
    def val(self, value: int):
        if value < 0:
            raise ValueError("Value must be greater than 0")
        print("Setting Value")
        self.__val = value

    def __repr__(self) -> str:
        return str(self.__val)
