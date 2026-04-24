class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            anagram = [0] * 26

            for j in range(len(string)):
                anagram[ord(string[j]) - ord('a')] += 1

            if tuple(anagram) in anagrams:
                anagrams[tuple(anagram)].append(string)
            else:
                anagrams[tuple(anagram)] = [string]
        

        return list(anagrams.values())
            