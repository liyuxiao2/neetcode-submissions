class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0 #extra parenth
        
        for i in s:
            if i == "(":
                res.append(i)
                cnt += 1
            elif i == ")" and cnt > 0:
                res.append(i)
                cnt -= 1
            elif i != ")":
                res.append(i)
        
        filtered = []

        for c in reversed(res):
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered.append(c)
            

        
        return "".join(reversed(filtered))

            

            