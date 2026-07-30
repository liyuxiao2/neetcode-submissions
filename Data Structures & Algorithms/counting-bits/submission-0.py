class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        bin_n = bin(n)

        for i in range(n+1):
            res.append(i.bit_count())
        
        return res


        