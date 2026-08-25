class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        cur = 0

        count = defaultdict(int)
        count[0] = 1

        for i in range(len(nums)):
            cur += nums[i]

            diff = cur - goal

            if diff in count:
                res += count[diff]

            count[cur] += 1
        return res