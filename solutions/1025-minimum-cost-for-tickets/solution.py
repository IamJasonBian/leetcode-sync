class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        

        '''
        |1|s|s|
        |7|s|s|
        |30|s|s|
        |s|s|s|


        Timeline Visualization:                                                     |
        |  Day:    1  2  3  4  5  6  7  8  9  10 ... 20                             |
        |  Travel: X     X  X  X  X           X                                      |
        |          ↑     └────7-day pass────┘  ↑                                      |
        |          │                           │                                       |
        |      1-day pass                  1-day pass                                 |
|                                            
                |
                            +----------------─┴─────────────────+
                            │                │                 │
                        1-day ($2)        7-day ($7)      30-day ($15)
                            │                │                 │
                        Day 4            Day 6             Day 20
                            │                │               (Done)
                    +-------┴-------+    +---┴----+
                    │             │     │        │
                1-day ($4)    7-day ($9) ...   30-day
                    │             │
                Day 6         Day 20
                    │          (Done)
            +------┴-----+
            │            │
        1-day ($6)   7-day ($11)
            │            │
        Day 7        Day 20
            │         (Done)
            │
        [Continue...]
                                  

        Initial Travel Days: [1,4,6,7,8,20]

                |1,$2|4|[6,7,8,20]|
                /         \         \
         |7,$9|20|[]|    |1,$4|6|[7,8,20]|    |30,$15|20|[]|
                         /          \
                |7,$11|20|[]|    |1,$6|7|[8,20]|
                                 /          \
                         |7,$13|20|[]|   |1,$8|8|[20]|
                                        /          \
                               |7,$15|20|[]|    |1,$10|20|[]|

        '''

        ticket_types = {
            0: 1,  # 1-day pass index
            1: 7,  # 7-day pass index
            2: 30  # 30-day pass index
        }
        
        travel_days = set(days)
        dp = [0] * (days[-1] + 1)
        
        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                min_cost = float('inf')
    
                for index, duration in ticket_types.items():
                    prev_day = max(0, day - duration)
                    min_cost = min(min_cost, dp[prev_day] + costs[index])
                dp[day] = min_cost




        return dp[days[-1]]
