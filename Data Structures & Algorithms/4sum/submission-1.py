class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()

        seen = set() # store tuples

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j+1, len(nums)-1

                first, second = nums[i], nums[j]
                while l < r:
                    if nums[l] + nums[r] + first + second > target:
                        r -=1
                    elif nums[l] + nums[r] + first + second < target:
                        l += 1
                    else:
                        if (first, second, nums[l], nums[r]) not in seen:
                            res.append([first, second, nums[l], nums[r]])
                            seen.add((first, second, nums[l], nums[r]))
                        l += 1
        return res

