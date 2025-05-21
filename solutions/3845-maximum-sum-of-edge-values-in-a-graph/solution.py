class Solution(object):
    def help(self, l, r, is_cycle):
        dq = deque()
        dq.append(r)
        dq.append(r)
        res = 0
        for a in range(r - 1, l - 1, -1):
            v = dq.popleft()
            res += v * a
            dq.append(a)
        if is_cycle:
            res += dq[0] * dq[1]
        return res

    def maxScore(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        m = len(edges)
        if m >= n:
            return self.help(1, n, True)
        else:
            return self.help(1, n, False)
