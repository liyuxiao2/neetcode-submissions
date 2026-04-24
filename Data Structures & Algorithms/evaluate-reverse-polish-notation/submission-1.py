class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current = []
        operators = ["*", "+", "-", "/"]
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                current.append(int(tokens[i]))
            else:
                first, second = current.pop(), current.pop()

                if(tokens[i] == "+"):
                    current.append(second+first)
                elif(tokens[i] == "-"):
                    current.append(second-first)
                elif(tokens[i] == "*"):
                    current.append(second*first)
                else:
                    current.append(int(second/first))
        return current[0]