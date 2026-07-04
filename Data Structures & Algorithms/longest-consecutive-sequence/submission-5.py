class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        longest = 0

        for num in uniq:
            if (num - 1) not in uniq:
                length = 1
                while (num + length) in uniq:
                    length += 1
                longest = max(longest, length)
        
        return longest
