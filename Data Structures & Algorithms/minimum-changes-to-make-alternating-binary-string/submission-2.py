class Solution:
    def minOperations(self, s: str) -> int:
        cur = cnt = 0

        for c in s:
            if int(c) != cur:
                cnt += 1
            cur ^= 1
        
        cur = 1
        cnt2 = 0

        for c in s:
            if int(c) != cur:
                cnt2 += 1
            cur ^= 1
        
        return min(cnt, cnt2)