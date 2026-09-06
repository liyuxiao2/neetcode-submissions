class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for s in strs:
            chars = [0] * 26

            for c in s:
                chars[ord('a') - ord(c)] += 1

            maps[tuple(chars)].append(s)
            
        return [val for val in maps.values()]