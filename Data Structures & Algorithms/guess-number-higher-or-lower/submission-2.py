# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 1, n

        while True:
            middle = (l+r) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                r = middle - 1
            else:
                l = middle + 1
        return -1 