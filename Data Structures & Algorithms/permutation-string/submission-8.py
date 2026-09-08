from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq1 = Counter(s1)
        freq2 = Counter()
        
        l = 0
        for r in range(len(s2)):
            freq2[s2[r]] += 1
            
            # Shrink the window if it exceeds s1 length
            if r - l + 1 > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
                
            if freq2 == freq1:
                return True
                
        return False
