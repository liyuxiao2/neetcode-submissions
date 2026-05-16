class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # p = 0
        # new_res = []

        # while p < len(word1) and p < len(word2):
        #     new_res.append(word1[p])
        #     new_res.append(word2[p])
        #     p += 1
        
        # if p < len(word1):
        #     return "".join(new_res) + word1[p:]
        # elif p < len(word2):
        #     return "".join(new_res) + word2[p:] 
        # else:
        #     return "".join(new_res)

    
        #More optimal SOL

        p = 0
        new_res = []

        while p < len(word1) or p < len(word2):
            if(p < len(word1)):
                new_res.append(word1[p])
            if(p < len(word2)):
                new_res.append(word2[p])
            p += 1
        
        return "".join(new_res)