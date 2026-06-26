class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = len(nums) + 1
        cur_sum = 0
        l = r = 0

        while r < len(nums):
            cur_sum += nums[r]
            r += 1
            
            while cur_sum >= target:
                min_l = min(min_l, r - l)
                cur_sum -= nums[l]
                l += 1
            
        return (min_l if min_l < len(nums) + 1 else 0)
