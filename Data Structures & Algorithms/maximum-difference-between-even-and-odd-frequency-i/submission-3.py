class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        even, odd = len(s), 0

        for val in count.values():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)


        return odd - even