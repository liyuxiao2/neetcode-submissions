class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False

        l, r = 0, len(s1)

        s1_perm = self.convertString(s1)

        while (r <= len(s2) and (r-l) >= len(s1)):
            perm = self.convertString(s2[l:r])

            if perm == s1_perm:
                return True
            
            l, r = l+1, r+1
        
        return False



    def convertString(self, s1: str) -> dict:
        perm = {}

        for char in s1:
            if char in perm:
                perm[char] += 1
            else:
                perm[char] = 1

        return perm