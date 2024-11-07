class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersect = []
        b_index = 0
        for interA in firstList:
            s1 = interA[0]
            e1 = interA[1]
            for index in range(b_index, len(secondList)):
                s2 = secondList[index][0]
                e2 = secondList[index][1]
                if s2 > e1:
                    break
                if e2 < s1:
                    b_index += 1
                    continue
                si = max(s1, s2)
                ei = min(e1, e2)
                intersect.append([si, ei])
                if e2 <= e1:
                    b_index += 1
        return intersect
