class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_str = set()
        l = 0

        for r in range(len(s)):
            while(s[r] in cur_str):
                cur_str.discard(s[l])
                l += 1
            cur_str.add(s[r])

            max_len = max(max_len, r-l+1)
            
        return max_len