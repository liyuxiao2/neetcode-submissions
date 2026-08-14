class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask != 0:
            sum_no_carry = a ^ b
            carry = (a & b) << 1

            a = sum_no_carry
            b = carry

        return a & mask if b > 0 else a
