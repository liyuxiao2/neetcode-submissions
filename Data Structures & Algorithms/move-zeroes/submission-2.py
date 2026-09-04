class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        s, f = 0, 0
        
        while f < len(nums) and s < len(nums):
            while s < len(nums) and nums[s] != 0:
                s += 1
            while f < len(nums) and (f < s or nums[f] == 0):
                f += 1
            
            if f < len(nums) and s < len(nums):
                nums[f], nums[s] = nums[s], nums[f]
                s, f = s + 1, f + 1
            
        
