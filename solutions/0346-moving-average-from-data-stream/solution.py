class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque(maxlen=size)
        
    def next(self, val: int) -> float:
        self.q.append(val)
        return sum(self.q) / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
