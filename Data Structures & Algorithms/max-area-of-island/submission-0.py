class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW = len(grid)
        COL = len(grid[0])
        dirc = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()

        def dfs(r,c, area):
            # check if out of bound
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return area
            # check if 0 or visited
            if grid[r][c] == 0 or (r,c) in visited:
                return area
            visited.add((r,c))
            area += 1
            #visit all neighbours
            for dr, dc in dirc:
                area = dfs(r+dr,c+dc,area)
            return area

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in visited or grid[r][c] == 0:
                    continue
                new_area = dfs(r,c,0)
                res = max(res, new_area)
        return res

            
            