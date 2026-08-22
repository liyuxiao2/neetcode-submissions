class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        #have as many 1's to the left most, leave 1 '1 at the end


        cnt = Counter(s)
        new_s = []

        while cnt["1"] > 1:
            new_s.append("1")
            cnt["1"] -= 1
        while cnt["0"] > 0:
            new_s.append("0")
            cnt["0"] -= 1
        
        new_s.append("1")

        return "".join(new_s)
