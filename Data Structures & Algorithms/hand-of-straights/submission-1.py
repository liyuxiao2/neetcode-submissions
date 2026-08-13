class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        hand.sort()

        for card in hand:
            if count[card]:
                for j in range(card, card + groupSize):
                    if not count[j]:
                        return False
                    count[j] -= 1
        return True
            