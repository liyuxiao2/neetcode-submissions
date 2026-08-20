class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t1, t2 = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            t1[s[i]] += 1
            t2[t[i]] += 1
        
        return t1 == t2

    