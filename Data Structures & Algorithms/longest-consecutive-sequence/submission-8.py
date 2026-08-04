class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_l = 0

        for n in nums:
            if n - 1 not in s:
                dec = 1  
                while n + dec in s:
                    dec += 1
                max_l = max(dec, max_l)
        
        return max_l

