class Solution:
    def maxTastiness(self, price: List[int], taste: List[int], maxAmount: int, maxCoupons: int) -> int:
        @cache
        def dfs(i: int, amount: int, coupons: int) -> int:
            return 0 if i >= len(price) else max(
                dfs(i + 1, amount, coupons),
                0 if amount < price[i] else taste[i] + dfs(i + 1, amount - price[i], coupons),
                0 if amount < price[i] // 2 or coupons == 0 else taste[i] + dfs(i + 1, amount - price[i] // 2, coupons - 1)
            )
        return dfs(0, maxAmount, maxCoupons)
