class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # at every index, we calculate the max product we can obtain
        # itself, or multiplying against previous maxes

        # [[2, 2], [8, 4], [-3, -24], 120]
        global_max = nums[0]
        c_min = nums[0]
        c_max = nums[0]

        for i in range(1, len(nums)):
            #start a new subarr, multiply by min or multiply by max
            c_max, c_min = max(nums[i] * c_max, nums[i] * c_min, nums[i]), min(nums[i] * c_max, nums[i] * c_min, nums[i])

            global_max = max(c_max, global_max)
        
        return global_max
        