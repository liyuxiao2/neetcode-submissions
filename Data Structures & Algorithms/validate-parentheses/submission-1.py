class Solution:
    def isValid(self, s: str) -> bool:
        valid = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                valid.append(i)
            else:
                if(valid == []):
                    return False
                res = valid.pop()

                if(res == '('):
                    if i != ')':
                        return False
                elif(res == '['):
                    if i != ']':
                        return False
                elif(res == '{'):
                    if i != '}':
                        return False
        return (valid == [])

