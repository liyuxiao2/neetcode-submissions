class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        in_degree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        done = 0

        for course, prereq in prerequisites:
            in_degree[prereq] += 1
            adj[course].append(prereq)
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        

        while q:
            val = q.popleft()
            done += 1

            for neighbor in adj[val]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return done == numCourses






            
            




