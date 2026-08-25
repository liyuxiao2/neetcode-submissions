class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = 0
        print(count)

        for key, val in count.items():
            if val == 1:
                return -1 
            
            total += math.ceil(val / 3)
        
        return total
            
            