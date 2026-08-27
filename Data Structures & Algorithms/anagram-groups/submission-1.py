class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)


        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            anag[tuple(count)].append(s)
        
        res = []
        for val in anag.values():
            res.append(val)

        return res

