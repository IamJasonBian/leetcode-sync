class Solution:
    def findMinMoves(self, machines):
        n, total = len(machines), sum(machines)

        if total%n != 0:
            return -1 

        target = total//n

        for i in range(n):
            machines[i] -= target

        cur_sum, max_sum, res = 0, 0, 0 

        for i in machines:
            cur_sum += i 
            max_sum = max(max_sum,abs(cur_sum))
            res = max(res,max_sum,i)

        return res
