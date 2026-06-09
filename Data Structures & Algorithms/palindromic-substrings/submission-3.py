class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]

                if substr in dp:
                    count += 1 
                elif substr == substr[::-1]:
                    dp.add(substr)
                    count += 1
        return count