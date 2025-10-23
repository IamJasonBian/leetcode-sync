from typing import List

class Solution:
      def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
          MOD = 10**9 + 7
          current = {(0, 0): 1}
          for i in range(len(group)):
              next_layer = {}
              states = list(current.items())

              for (members, prof), count in states:
                  key1 = (members, prof)
                  next_layer[key1] = (next_layer.get(key1, 0) + count) % MOD
                  if members + group[i] <= n:
                      new_members = members + group[i]
                      new_profit = min(prof + profit[i], minProfit)
                      key2 = (new_members, new_profit)
                      next_layer[key2] = (next_layer.get(key2, 0) + count) % MOD

              current = next_layer
          result = 0
          for (members, prof), count in current.items():
              if prof >= minProfit:
                  result = (result + count) % MOD

          return result
