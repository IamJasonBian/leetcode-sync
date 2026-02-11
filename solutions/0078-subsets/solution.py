from typing import List

class Solution:
      def subsets(self, nums: List[int]) -> List[List[int]]:

        '''

            O(1)

                [1]
                [1,2,3]
                [2,3]
                [3,3]

            [[], [1], [2], [1,2], [1,2,3]]

            backtrack(0)
                0, 1, 2
                 path = [[0, 1, 2]]
                    path = [[1, 2]]

                   1  2
                    path = [[1, 2]]
                         2
            
            backtrack(1)
                1, 2
                path = [[1, 2, 3]]

               
            backtrack(2)
                1, 2
                path = [[1, 2]]

            backtrack(3)
                2
                path = [[2]]

            [[], [1], [2], [1,2]]


        Permuating

            |  |  | - add to res
            |  |  |
            |  |  |

        The start stays steady (does not move)
        How to fix the popping - the pop happens when you get to the end of an iteration

        Iterations - 

        * 0 to 2 - [1,2,3]
        * 1 to 2 - 
        * 2 to 2 

        FiFo to guarantee symmetry 

        '''
      
        res, path = [], []
        n = len(nums)

        def backtrack(start: int):
            res.append(path.copy())

            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res
