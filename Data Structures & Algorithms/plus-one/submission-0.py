class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        new = [0 for i in range(len(digits))]
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry == 10:
                new[i] = 0
            else:
                new[i] =  digits[i] + carry
                carry = 0
        
        if carry == 1:
            new = [carry] + new
        
        return new