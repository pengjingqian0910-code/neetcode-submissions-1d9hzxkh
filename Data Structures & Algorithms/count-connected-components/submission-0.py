class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range (n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count