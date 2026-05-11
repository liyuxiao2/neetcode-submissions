class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = [char for char in strs[0]]

        for s in strs[1:]:
            if s == "":
                return ""
            if len(s) < len(longest):
                longest = longest[:len(s)]
            
            for i in range(len(longest)):
                if s[i] != longest[i]:
                    longest = longest[:i]
                    break
                else:
                    i += 1
        
        return "".join(longest)
            