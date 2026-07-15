class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        chars = set()
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] in d or s[i] in chars:
                if (s[i] in chars and pattern[i] not in d) or not (d[pattern[i]] == s[i] and pattern[i] not in d.values()):
                    return False
            else:
                chars.add(s[i])
                d[pattern[i]] = s[i]
        
        return True
