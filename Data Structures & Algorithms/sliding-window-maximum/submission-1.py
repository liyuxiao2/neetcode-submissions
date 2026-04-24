class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # l, r = 0, k
        # res = []

        # while r < len(nums) + 1:
        #     window = nums[l:r]

        #     res.append(max(window))

        #     l, r = l + 1, r + 1

        
        # return res
        # #correct but inefficient, max(window) is O(k)

        res = []
        dq = deque()

        for i in range(len(nums)):

            #if we exceed k
            if dq and dq[0] <= i - k:
                dq.popleft()

            #remove smaller vals
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
        return res