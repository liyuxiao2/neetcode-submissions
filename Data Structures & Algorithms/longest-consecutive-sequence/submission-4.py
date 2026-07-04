class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        max_l = 1
        uniq = set(nums)

        for num in uniq:
            if (num - 1) not in uniq:
                cur = num
                while (cur + 1) in uniq:
                    longest += 1
                    cur += 1
            max_l = max(max_l, longest)
            longest = 1
        
        return max(max_l, longest)
