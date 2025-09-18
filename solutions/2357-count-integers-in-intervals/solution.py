from bisect import bisect_left, bisect_right

class CountIntervals:
    def __init__(self):
        self.L = []
        self.R = []
        self.total = 0

    def add(self, left: int, right: int) -> None:
        if not self.L:
            self.L.append(left)
            self.R.append(right)
            self.total += right-left+1
        else:
            idx_l, idx_r = bisect_left(self.R, left), bisect_right(self.L, right)
            lm, rm = left, right
            while idx_l < idx_r:
                l1 = self.L.pop(idx_r-1)
                r1 = self.R.pop(idx_r-1)
                self.total -= r1-l1+1
                lm = min(lm, l1)
                rm = max(rm, r1)
                idx_r -= 1
            self.L.insert(idx_l, lm)
            self.R.insert(idx_l, rm)
            self.total += rm-lm+1
        
    def count(self) -> int:
        return self.total
