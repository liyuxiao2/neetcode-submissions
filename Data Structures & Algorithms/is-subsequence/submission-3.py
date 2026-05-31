class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False

        p1 = p2 = 0

        while p2 < len(t) and p1 < len(s):
            if t[p2] == s[p1]:
                p1 += 1
            p2 += 1
        
        print(p1, p2)
        return (p1 == len(s))