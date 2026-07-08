class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        p1 = p2 = 0

        while p1 < n and p2 < m:
            if abbr[p2] == "0":
                return False
                
            if abbr[p2].isdigit():
                subLen = 0
                while p2 < m and abbr[p2].isdigit():
                    subLen = subLen * 10 + int(abbr[p2])
                    p2 += 1
                p1 += subLen
            elif abbr[p2] != word[p1]:
                return False
            else:
                p1 += 1
                p2 += 1
        
        return p1 == n and p2 == m
