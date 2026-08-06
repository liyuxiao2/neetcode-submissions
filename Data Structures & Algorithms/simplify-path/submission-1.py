class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = []

        #if we see a .., pop out
        #if we see a ., do nothing
        #if we see / or more keep it the same, we can skip extra /
        #else we add the current string to the directory

        for c in path + "/":
            if c == "/":
                if cur == [".", "."]:
                    if stack:
                        stack.pop()
                elif cur != [] and cur != ["."]:
                    stack.append("".join(cur))
                cur = []
            else:
                cur.append(c)
        
        return "/" + "/".join(stack)
        



