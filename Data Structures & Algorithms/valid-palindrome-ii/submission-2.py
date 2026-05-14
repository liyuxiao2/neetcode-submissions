class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                left = s[l + 1: r + 1]
                right = s[l: r]
                return left == left[::-1] or right == right[::-1]
            else:
                l, r = l + 1, r - 1
        return True