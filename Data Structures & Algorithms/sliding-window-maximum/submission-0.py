class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        res = []

        while r < len(nums) + 1:
            window = nums[l:r]

            res.append(max(window))

            l, r = l + 1, r + 1

        
        return res