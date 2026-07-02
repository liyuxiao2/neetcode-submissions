class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        items = {}
        count = 0
        for i in text:
            if i in "balon":
                items[i] = items.get(i, 0) + 1
        
        while True:
            if items.get("b", 0)  >= 1 and items.get("a", 0) >= 1 and items.get("l", 0) >= 2 and items.get("o", 0) >= 2 and items.get("n", 0) >= 1:
                items["b"] -= 1
                items["a"] -= 1
                items["l"] -= 2
                items["o"] -= 2
                items["n"] -= 1
                count += 1
            else:
                return count
