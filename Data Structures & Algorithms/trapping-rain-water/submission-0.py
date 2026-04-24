class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0, len(height)-1
        lh,lr = height[l], height[r]
        res = 0
        while l<r:
            if lh < lr:
              l += 1
              lh = max(lh, height[l])
              res += lh - height[l]
            else:
                r -= 1
                lr = max(lr, height[r])
                res += lr - height[r]
        return res