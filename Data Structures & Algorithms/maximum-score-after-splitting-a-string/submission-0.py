class Solution:
    def maxScore(self, s: str) -> int:
        #if we see a zero -1, else if we see a 1 +1,
        #prefix/suffix 

        n = len(s)

        zero, one = [0] * n, [0] * n

        if s[0] == '0':
            zero[0] = 1
        for i in range(1, n):
            zero[i] = zero[i-1]
            if s[i] == '0':
                zero[i] += 1
        
        if s[n - 1] == '1':
            one[n- 1] = 1
        for i in range(n - 2, -1, - 1):
            one[i] = one[i+1]
            if s[i] == '1':
                one[i] += 1
            
        res = 0

        for i in range(1, n):
            res = max(res, zero[i - 1] + one[i])

        return res
