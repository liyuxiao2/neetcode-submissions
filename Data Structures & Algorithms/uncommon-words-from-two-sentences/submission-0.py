class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(" "), s2.split(" ")

        count = Counter(s1) + Counter(s2)
        
        res = [key for key, val in count.items() if val == 1]

        return res
