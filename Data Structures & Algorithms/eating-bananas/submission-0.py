class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #the upper bound would be the max in the list
        #takes ciel(x/k) to finish 1 pile
        #it must also be less than h in the end'
        l, r = 1, max(piles)
        res = r

        while(l <= r):
            k = (l+r) // 2
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            
            if hours <= h:
                res = min(res, k)
                r = k -1
            else:
                l = k+1
        
        return res



