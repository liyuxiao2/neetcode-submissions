class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = cur_one = 0

        for num in nums:
            if num == 1:
                cur_one += 1
            else:
                max_one, cur_one = max(cur_one, max_one), 0
        
        return max(max_one, cur_one)