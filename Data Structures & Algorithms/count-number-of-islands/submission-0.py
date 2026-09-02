class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j, count):
            if i < 0  or i >= m or j < 0  or j >= n:
                return False
            elif grid[i][j] == "0": 
                return False

            grid[i][j] = "0"
            
            count += dfs(i+1, j, count)
            count += dfs(i-1, j, count)
            count += dfs(i, j+1, count)
            count += dfs(i, j-1, count)

            return True

        count = 0
        for i in range(m):
            for j in range(n):
                if dfs(i,j,count):
                    count += 1

        return count
                 
            

        

        