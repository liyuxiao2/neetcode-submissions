class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        distinct = set(nums)
        print(distinct)

        for i in range(1, len(nums) + 1):
            if i not in distinct:
                res.append(i)
        
        return res
        