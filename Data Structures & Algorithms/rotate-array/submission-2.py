class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        count = ptr = 0

        while count < len(nums):
            cur = ptr
            prev = nums[ptr]
            while True:
                index = (cur + k) % len(nums)
                nums[index], prev = prev, nums[index]
                cur = index

                count += 1

                if cur == ptr:
                    break
            ptr += 1
