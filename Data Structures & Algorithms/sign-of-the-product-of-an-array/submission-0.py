class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_c = 0

        for i in range(len(nums)):
            if nums[i] < 0:
                neg_c += 1
            if nums[i] == 0:
                return 0
        
        return -1 if neg_c % 2 != 0 else 1