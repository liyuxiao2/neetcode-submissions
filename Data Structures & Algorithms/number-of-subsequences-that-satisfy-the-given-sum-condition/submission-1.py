class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #n log n

        nums.sort()
        mod = 10**9 + 7

        l, r = 0, len(nums) - 1

        res = 0

        while l <= r:
            if nums[r] + nums[l] <= target:
                res += pow(2, r - l, mod)
                res %= mod
                l += 1
            else:
                r -= 1
        
        return res
