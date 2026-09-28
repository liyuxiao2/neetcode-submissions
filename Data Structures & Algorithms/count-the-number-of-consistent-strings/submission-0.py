class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set(allowed)
        count = 0

        for w in words:
            stop = False
            for i in w:
                if i not in allowed:
                    stop = True
                    break
            if not stop:
                count += 1
        return count