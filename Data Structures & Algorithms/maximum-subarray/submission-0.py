class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = max_sum = nums[0] #max
        for i in range(1, len(nums)):
            max_sum = max(nums[i], max_sum + nums[i])

            if max_sum > max_global:
                max_global = max_sum
        return max_global
        
