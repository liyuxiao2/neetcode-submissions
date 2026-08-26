class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #pre fix, we can calculate the prefix sum at each step

        # [2, 1, 3, 5]

        # if lets say the current goal = prefix - diff
        # we can rearrange -> diff = prefix - goal

        # if we find that the difference exists in the array, we can add that to our res

        #if the diff is 0, our prefix is already good, so default should be {0: 1}

        prefix = defaultdict(int)
        prefix[0] = 1
        res, cur_s = 0, 0

        for n in nums:
            cur_s += n

            diff = cur_s - k

            if diff in prefix:
                res += prefix[diff]
            
            prefix[cur_s] += 1
        
        return res
