class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        seen = {i: 0 for i in range(1, len(nums) + 1)}

        for num in nums:
            seen[num] += 1
        
        for key, value in seen.items():
            if value == 0:
                res[1] = key
            if value == 2:
                res[0] = key
        return res