class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        in_degree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        res = []

        for course, prereq in prerequisites:
            in_degree[prereq] += 1
            adj[course].append(prereq)
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            val = q.popleft()
            res.append(val)

            for neighbor in adj[val]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return res[::-1] if len(res) == numCourses else []