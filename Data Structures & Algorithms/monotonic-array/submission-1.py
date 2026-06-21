class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_dec = False

        if nums[0] < nums[-1]:
            is_dec = True

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i] and is_dec:
                return False
            elif nums[i-1] < nums[i] and not is_dec:
                return False
        return True