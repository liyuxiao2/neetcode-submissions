class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                stars.append(i)
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while left and stars:
            v1, v2 = left.pop(), stars.pop()

            if v1 > v2:
                return False

        

        return not left
 