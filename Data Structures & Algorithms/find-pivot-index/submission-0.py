class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r_sum = 0
        l_sum = sum(nums[1:])
        index = 1

        while index < len(nums) and r_sum != l_sum:
            r_sum += nums[index - 1]
            l_sum -= nums[index]
            index += 1
        
        return index - 1 if r_sum == l_sum else -1
