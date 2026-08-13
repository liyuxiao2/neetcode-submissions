class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_i = {char: i for i, char in enumerate(s)}

        res = []

        end = size = 0

        for i, c in enumerate(s):
            size += 1

            if last_i[c] > end:
                end = last_i[c]
            
            if i == end:
                res.append(size)
                size = 0
            
        return res