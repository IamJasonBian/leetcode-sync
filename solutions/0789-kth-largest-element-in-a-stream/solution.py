class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min=[]
        self.max=[]
        self.k=k
        heapify(self.min)
        heapify(self.max)
        for v in nums:
            heappush(self.max,-v)
        while self.max and len(self.min)<k:
            heappush(self.min,-heappop(self.max))
    def add(self, val: int) -> int:
        if len(self.min)<self.k:
            heappush(self.min,val)
        else:
            if self.max and -self.max[0]>=val:
                heappush(self.max,-val)
            else:
                heappush(self.min,val)
                if len(self.min)>self.k:
                    heappush(self.max,-heappop(self.min))
        return self.min[0]

