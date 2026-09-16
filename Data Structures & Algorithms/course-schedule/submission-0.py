class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visiting = set()
        visited = set()

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course):
            if course in visiting:
                return False
            elif course in visited:
                return True
            else:
                visiting.add(course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True