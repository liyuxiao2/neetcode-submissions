class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 1, nums[0]

        for num in nums[1:]:
            if num == majority:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                count, majority = 1, num
        
        return majority