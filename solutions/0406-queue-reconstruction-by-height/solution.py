class Solution:
    # O(n^2) time | O(n) space
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []

        # Sort people by height and position in the queue
        # Key: (-height, k) to descending height and ascending k
        people.sort(key=lambda x: (-x[0], x[1]))

        for p in people:
            _, position = p
            res.insert(position, p)
        return res
