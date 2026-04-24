class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1

            init = nums[i]
            while l < r:
                if nums[l]+nums[r] + init > 0:
                    r -=1
                elif nums[l]+nums[r] + init < 0:
                    l += 1
                else:
                    if (([nums[l],nums[r], init]) not in res):
                        res.append([nums[l],nums[r], init])
                    l += 1

        return res