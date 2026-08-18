class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = cur_len = 0

        begin = end = 0
        seen = set()

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
            else:
                max_len = max(max_len, len(seen))
                while s[end] in seen and begin < end:
                    seen.remove(s[begin])
                    begin += 1
        return max(max_len, len(seen))
                

                