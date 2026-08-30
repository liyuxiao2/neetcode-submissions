class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in s_dict and s_dict[c1] != c2) or (c2 in t_dict and t_dict[c2] != c1):
                return False
            
            s_dict[c1] = c2
            t_dict[c2] = c1
        
        return True
            