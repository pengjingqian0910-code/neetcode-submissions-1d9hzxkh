class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == '0'):
                return 0
            
            visit.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r ,c + 1)
            dfs(r ,c - 1)
            return 1
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit:
                    count += dfs(i,j)
        return count



        