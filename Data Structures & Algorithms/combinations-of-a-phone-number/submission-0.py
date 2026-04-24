class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits == ""):
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur):
            if(i == len(digits)):
                res.append(cur)
                return
            
            cur_d = digits[i]
            
            for j in digitToChar[cur_d]:
                dfs(i + 1, cur + j)

        dfs(0, "")
        
        return res
        
