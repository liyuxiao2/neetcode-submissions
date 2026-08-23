class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_s = nums[0]
        cur_s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_s += nums[i]
            else:
                cur_s = nums[i]
            
            max_s = max(max_s, cur_s)

        return max_s
