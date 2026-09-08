class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = Counter(s1)

        window = {}
        l = 0

        for i in range(len(s2)):
            print(window)
            if i >= len(s1):
                if window == freq:
                    return True
                
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]
                
                l += 1
            window[s2[i]] = 1 + window.get(s2[i], 0)
        
        print(window)
        return window == freq