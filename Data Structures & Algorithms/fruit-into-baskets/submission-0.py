class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2 baskets, fruits[i], indicates the type of fruit

        #we can start at any tree, we must pick from every tree starting from that to whatever we cant

        #sliding window, we store a hash map and a maximum fruit

        count = defaultdict(int)

        l = r = 0
        max_c = 0

        while r < len(fruits):
            count[fruits[r]] += 1

            while len(count) > 2:
                print(count, l)
                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            

            max_c = max(max_c, r - l + 1)
            r += 1
        
        print(l, r)
        print(count)
        return max_c