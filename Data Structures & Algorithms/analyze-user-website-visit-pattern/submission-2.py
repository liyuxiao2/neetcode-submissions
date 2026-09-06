class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        user_pattern = defaultdict(list)
        count = defaultdict(int)

        for i in range(len(username)):
            user_pattern[username[i]].append((timestamp[i], website[i]))

        for key, tuple_list in user_pattern.items():
            tuple_list.sort(key=lambda x: x[0])
            user_pattern[key] = [w for t, w in tuple_list]
        
        subpatterns = defaultdict(int)

        for user in user_pattern:
            seen = set()
            cur = user_pattern[user]
            #u1: ["a", "b", "x", "c", "d"]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        seen.add((cur[i], cur[j], cur[k]))

            for p in seen:
                subpatterns[p] += 1
                

        max_c = 0
        res = ()

        for value, count in subpatterns.items():
            if count > max_c:
                res = value
                max_c = count
            elif count == max_c:
                res = min(res, value)
        return list(res)

            
            
            


            
            

