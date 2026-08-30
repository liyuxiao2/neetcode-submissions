class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0

        for num, c in count.items():
            total += c * (c - 1) // 2
        
        return total