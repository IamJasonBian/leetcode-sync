class PhoneDirectory:
    # O(n)
    def __init__(self, maxNumbers: int):
        self.__slots = set(range(maxNumbers))

    # O(1)
    def get(self) -> int:
        if not self.__slots:
            return -1
        return self.__slots.pop()

    # O(1)
    def check(self, number: int) -> bool:
        return number in self.__slots

    # O(1)
    def release(self, number: int) -> None:
        self.__slots.add(number)
