class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        n = int(bin(n)[2:])
        
        while n > 0:
            l_most = n % 10

            if l_most ^ 0 == 1:
                total += 1
            
            n = n // 10
        
        return total