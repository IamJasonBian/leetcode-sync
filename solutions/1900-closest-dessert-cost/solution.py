class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        return min(
            reduce(lambda cst, t: cst | {c + t for c in cst}, toppingCosts * 2, set(baseCosts)),
            key=lambda x: (abs(x - target), x))
