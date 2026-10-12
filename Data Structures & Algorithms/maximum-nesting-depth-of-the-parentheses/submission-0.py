class Solution:
    def maxDepth(self, s: str) -> int:
        res, cur = 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                cur += 1
            elif s[i] == ")":
                cur -= 1
            res = max(res, cur)
        return res

        