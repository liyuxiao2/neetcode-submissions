class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for s in strs:
            maps[tuple(sorted(s))].append(s)

    
        return [val for val in maps.values()]