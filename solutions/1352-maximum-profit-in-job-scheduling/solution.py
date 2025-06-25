class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):

        dp = [0]
        cur_end = [0] 
        n = len(endTime)       

        #Binary search to get the closest non overlapping job
        def BinarySearch(v):
            l = 0
            r = len(cur_end)-1

            ans = 0
            while l <= r:
                mid = l + (r-l)//2

                if cur_end[mid]<=v:
                    ans = mid
                    l = mid+1
                else:
                    r = mid-1
            return ans

        # Sort based on the endtime
        jobs = [
            [endTime[i],startTime[i],profit[i]] for i in range(n)
        ]
        jobs.sort()


        for i in range(n):
            e,s,p = jobs[i]
        

            idx = BinarySearch(s)
            
            # Is prev overlapping job more profitable or the this one with non overlapping job?
            dp.append(
                max(
                    p + dp[idx],
                    dp[-1]
                )
            )
          
            cur_end.append(e)
        return dp[-1]
