class CountFromBy:
    def __init__(self, val=0, incr=1) ->'object':
        self.val = val
        self.incr = incr
        

    def increase(self) -> None:
        self.val += self.incr

    def __str__(self) -> str:
        return str(self.val)
