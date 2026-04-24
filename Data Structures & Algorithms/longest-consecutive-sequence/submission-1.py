class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniq_nums = set(nums)

        for num in uniq_nums:
            length = 0
            if not (num - 1) in uniq_nums:
                while (num+length) in uniq_nums:
                    length += 1
            
            longest = max(longest, length)

        return longest