class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #just a prefix sum

        # -1, 0, 1, 2, 3, 4, 5, 6 etc etc
        prefix = [0]
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        prefix = prefix[1:]

        res = []
        for q in queries:
            l, r = q

            left_val = prefix[l - 1] if l > 0 else 0

            total = prefix[r] - left_val

            res.append(total)
        
        return res

