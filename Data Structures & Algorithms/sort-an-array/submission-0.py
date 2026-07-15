class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        #split
        mid = len(nums) // 2

        l1 = self.sortArray(nums[:mid])
        l2 = self.sortArray(nums[mid:])

        res = self.merge(l1, l2)

        return res


    def merge(self, l1, l2) -> List[int]:
        p1 = p2 = 0
        res = []

        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] >= l2[p2]:
                res.append(l2[p2])
                p2 += 1
            else:
                res.append(l1[p1])
                p1 += 1
        
        res += l1[p1:] + l2[p2:]
        print(res)

        return res

    
