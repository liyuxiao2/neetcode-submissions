class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for x in range(n+1, len(nums)): 
                if nums[n] + nums[x] == target: 
                    return [n,x]