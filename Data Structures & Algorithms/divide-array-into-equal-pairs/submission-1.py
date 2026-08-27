class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        cur_c = 0

        for _, val in count.items():
            if val % 2 != 0:
                return False
            cur_c += val // 2
        
        return cur_c == len(nums) // 2