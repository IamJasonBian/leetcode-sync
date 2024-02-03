import heapq as hq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We need to permuate through each task and cycle to calculate the difference in permutations
        count = Counter(tasks)

        #Array implementation of maxHeap 
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q: 

            #processing -> increment time by 1
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:

                    #time + n (backoff time)
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        

