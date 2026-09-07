class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #pos, neg -> if nums[pos] > 0 and pos % 2 != 0, continue
        #else we increase the negative until we find one, swap
        # pos += 1

        #if nums[neg] < 0 and neg % 2 == 0, continue

        pos, neg = 0, 1
        res = [None for _ in range(len(nums))]

        for _, num in enumerate(nums):
            if num > 0:
                res[pos] = num
                pos += 2
            elif num < 0:
                res[neg] = num
                neg += 2
        
        return res
                


