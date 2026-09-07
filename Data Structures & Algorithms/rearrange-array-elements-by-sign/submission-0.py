class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #pos, neg -> if nums[pos] > 0 and pos % 2 != 0, continue
        #else we increase the negative until we find one, swap
        # pos += 1

        #if nums[neg] < 0 and neg % 2 == 0, continue

        pos, neg = 0, 0
        res = []

        while pos < len(nums) or neg < len(nums):
            while pos < len(nums) and nums[pos] < 0:
                pos += 1
            
            while neg < len(nums) and nums[neg] > 0:
                neg += 1

            if not res or (res[-1] < 0 and pos < len(nums)):
                res.append(nums[pos])
                pos += 1
            elif (res[-1] > 0 and neg < len(nums)):
                res.append(nums[neg])
                neg += 1
        
        return res
                


