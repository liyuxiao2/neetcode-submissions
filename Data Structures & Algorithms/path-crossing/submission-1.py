class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = [0, 0]

        seen = set()
        seen.add(tuple(cur))

        for p in path:
            match p:
                case "N":
                    cur[1] += 1
                case "E":
                    cur[0] += 1
                case "S":
                    cur[1] -= 1
                case "W":
                    cur[0] -= 1
            if tuple(cur) in seen:
                return True
            seen.add(tuple(cur))
        return False
        