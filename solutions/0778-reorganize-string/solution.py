class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)
        # heap the letters
        # maxHeap = [n for n in count.values()]
        res = ""
        stack = []

        # because it's negative hence maxHeap
        maxHeap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)
        # print(heapq.heappop(maxHeap)[1])

        while maxHeap:

            for _ in range(2):
            # run twice?
            # don't return res, use ""
                if not maxHeap and stack: return ""
                if maxHeap:
                    count, char = heappop(maxHeap)

                    # interchange logic
                    res += char

                    # adding back to the stack (full tuple after popping)
                    if count <-1: stack.append((count + 1, char))

            while stack: heappush(maxHeap, stack.pop())

        return res
