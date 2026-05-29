class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        l, r = 0, 0
        count = 0

        max_jump = nums[0]

        while l + max_jump < len(nums) - 1:
            print(l, max_jump)
            count += 1
            cur_jump = 0
            for i in range(l + 1, l + max_jump + 1):
                if (cur_jump -  i) < nums[i] or (cur_jump == nums[i] and r < i):
                    cur_jump = max(cur_jump, nums[i])
                    r = i

            l = r
            max_jump = cur_jump

        return count + 1
            

