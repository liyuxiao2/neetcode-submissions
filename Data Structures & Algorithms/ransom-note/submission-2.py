class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char = Counter(magazine)

        for c in ransomNote:
            if char[c]<= 0:
                return False
            char[c] -= 1
        
        return True