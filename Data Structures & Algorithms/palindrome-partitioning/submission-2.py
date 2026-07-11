class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #we choose current char

        #if char trhat we add to the substr is a palindrome, we add it to the res
        #thats path1, path 2 is we choose to start the new palindrome at that char

        #2 paths

        #adding to the substr, backtrack to start the new palindrome at that char
        cur = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                sub_str = s[i:j+1]

                if sub_str == sub_str[::-1]:
                    cur.append(sub_str)
                    dfs(j + 1)
                    cur.pop()
        dfs(0)

        return res

