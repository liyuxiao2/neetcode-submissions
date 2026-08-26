class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_l = 0

        inc, dec = 1, 1

        for i in range(1, len(nums)):
            print(max_l, dec, inc)
            max_l = max(max_l, dec, inc)
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1
            
        return max(max_l, inc, dec)
                