class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_str = set()
        l, r = 0,0

        while r < len(s):
            if(s[r] in cur_str):
                cur_str.clear()
                max_len = max((r-l), max_len)
                l += 1
                r = l
            else:
                cur_str.add(s[r])
                r += 1
        
        return max(max_len, (r-l))