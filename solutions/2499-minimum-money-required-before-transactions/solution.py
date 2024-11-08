class Solution:
    def minimumMoney(self, A: List[List[int]]) -> int:
        spend = 0
        cashback = 0
        cost = 0
        for i, j in A:
            if i > j:
                spend += i - j
                cashback = max(cashback, j)
            else:
                cost = max(cost, i)
        return spend + max(cashback, cost)
