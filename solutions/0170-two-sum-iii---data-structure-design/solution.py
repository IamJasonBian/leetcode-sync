class TwoSum:

    def __init__(self):
        self.nums={}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number]+=1
        else:
            self.nums[number]=1

    def find(self, value: int) -> bool:
        for i in self.nums:
            if value-i in self.nums:
                if i==value-i and self.nums[i]==1:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
