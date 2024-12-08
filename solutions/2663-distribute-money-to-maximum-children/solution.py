class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        ans = min(money // 7, children)
        money -= 7 * ans
        remainingChildren = children - ans
        if remainingChildren == 1 and money == 3:
            ans -= 1
        elif remainingChildren == 0 and money > 0:
            ans -= 1
        return ans
