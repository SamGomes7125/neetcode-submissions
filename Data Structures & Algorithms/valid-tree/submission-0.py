class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            visited.add(node)

            for next_node in graph[node]:
                if next_node == parent:
                    continue

                if next_node in visited:
                    return False

                if not dfs(next_node, node):
                    return False

            return True
                    
            
        if not dfs(0, -1):
                return False
                
        return len(visited) == n
        


        