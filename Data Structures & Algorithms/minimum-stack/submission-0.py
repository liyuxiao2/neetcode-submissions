class MinStack:

    def __init__(self):
        self.array = []
        self.cur_min = []

    def push(self, val: int) -> None:
        self.array.append(val)
        vals = min(val, self.cur_min[-1] if self.cur_min else val)
        self.cur_min.append(vals)
        

    def pop(self) -> None:
        self.array.pop()
        self.cur_min.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.cur_min[-1]
