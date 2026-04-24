'''

Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.


'''


from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        based on the length of the string we will shift every character by len(strs)

        """
        new_total = ""
        for i in range(len(strs)):
            new_total += str(len(strs[i])) + "#" + strs[i]

        return new_total

    def decode(self, s: str) -> List[str]:
        """
        decode it by the same length
        """
        reverted_list = []
        count = 0
        while count < len(s):
            j = count

            while s[j] != "#":
                j += 1

            len_str = int(s[count:j])

            count = j + 1
            j = count + len_str
            
            reverted_list.append(s[count:j])
            
            count = j

        return reverted_list
    