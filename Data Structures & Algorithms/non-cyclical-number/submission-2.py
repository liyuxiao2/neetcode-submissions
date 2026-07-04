class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sums = 0

        while n != 1:
            while n / 10 > 0:
                sums += (n % 10) ** 2
                n //= 10
            if sums == 1:
                return True
            if sums in seen:
                return False
            n = sums
            seen.add(n)
            sums = 0
        return n == 1