from collections import deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for card in sorted(count.keys()):
            if count[card] == 0:
                continue
            num_groups = count[card]
            for i in range(groupSize):
                next_card = card + i
                if count[next_card] < num_groups:
                    return False
                count[next_card] -= num_groups

        print(count[next_card])

        return True

