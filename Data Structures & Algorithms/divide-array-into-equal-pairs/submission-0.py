class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums) // 2

        count = Counter(nums)

        cur_c = 0

        for key, val in count.items():
            if val % 2 != 0:
                return False
            cur_c += val // 2
        
        return cur_c == n