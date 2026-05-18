class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_score = []

        for i in operations:
            match i:
                case "D":
                    total_score.append(total_score[-1] * 2)
                case "+":
                    total_score.append(total_score[-1] + total_score[-2])
                case "C":
                    total_score.pop()
                case _:
                    total_score.append(int(i))
        return sum(total_score)
