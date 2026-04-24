class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count = {}
        
        arr = []

        for i in nums:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1


        for key, val in char_count.items():
            arr.append([val,key])
        
        arr.sort()

        res = []

        while k > 0:
            res.append(arr.pop()[1])
            k -= 1

        return res



