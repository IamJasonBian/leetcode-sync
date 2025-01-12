import bisect
class Allocator:
    def merge(self):
        i, j = 0, 1
        leng = len(self.ava)
        while j < leng:
            if self.ava[i][0] + self.ava[i][1] == self.ava[j][0]:
                self.ava[i][1] += self.ava[j][1]
                self.ava[j] = -1
            else:
                i = j
            j += 1
        self.ava = [x for x in self.ava if x != -1]

    def __init__(self, n: int):
        self.diction = defaultdict(list)
        self.ava = [[0, n]]

    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.ava)):
            if self.ava[i][1] < size: continue
            self.diction[mID].append([self.ava[i][0], size])
            res = self.ava[i][0]
            self.ava[i][0] += size
            self.ava[i][1] -= size
            return res
        return -1

    def freeMemory(self, mID: int) -> int:
        res = 0
        for interval in self.diction[mID]:
            bisect.insort(self.ava, interval)
            res += interval[1]
        self.merge()
        del self.diction[mID]
        return res
