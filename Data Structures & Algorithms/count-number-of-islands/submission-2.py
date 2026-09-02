class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0
        dr = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(r,c):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            #visit all neighbours
            bfs(r+dr[0][0],c+dr[0][1])
            bfs(r+dr[1][0],c+dr[1][1])
            bfs(r+dr[2][0],c+dr[2][1])
            bfs(r+dr[3][0],c+dr[3][1])
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0" or (r,c) in visited:
                    continue
                island += 1
                bfs(r,c)
        
        return island

            