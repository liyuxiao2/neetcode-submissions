class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}

        for i in arr:
            seen[i] = seen.get(i, 0) + 1
        
        for key, val in seen.items():
            if val == 1:
                k -= 1
            if k == 0:
                return key
        return ""