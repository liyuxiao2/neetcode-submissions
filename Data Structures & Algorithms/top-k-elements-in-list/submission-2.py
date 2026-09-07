class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)


        res = [[] for _ in range(len(nums) + 1)]

        for nm, cnt in count.items():
            res[cnt].append(nm)

        
        final = []

        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                final.append(num)

                if len(final) == k:
                    return final