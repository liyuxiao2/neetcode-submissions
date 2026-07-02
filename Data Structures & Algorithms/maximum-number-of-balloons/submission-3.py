class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        items = defaultdict(int)
        for i in text:
            if i in "balon":
                items[i] += 1
        
        if len(items) < 5:
            return 0

        items["l"] //= 2
        items["o"] //= 2

        return min(items.values())
