class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.cancelled = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:

        while self.riders and self.riders[0] in self.cancelled:
            self.cancelled.discard(self.riders.popleft())

        if self.riders and self.drivers:
            d = self.drivers.popleft()
            r = self.riders.popleft()
            return d, r
        return (-1,-1)


    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.cancelled.add(riderId)

'''

class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.cancelled = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        # Skip cancelled riders at the front
        while self.riders and self.riders[0] in self.cancelled:
            self.cancelled.discard(self.riders.popleft())

        if self.riders and self.drivers:
            r = self.riders.popleft()
            d = self.drivers.popleft()
            return [d, r]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        self.cancelled.add(riderId)  # O(1) instead of O(n)

'''
