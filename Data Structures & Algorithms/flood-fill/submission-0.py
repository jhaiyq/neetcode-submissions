class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return 
        m = len(image)
        n = len(image[0])
        def dfs(i,j, color, ori_color):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if image[i][j] != ori_color:
                return
            
            image[i][j] = -1

            dfs(i+1,j,color,ori_color)
            dfs(i-1,j,color,ori_color)
            dfs(i,j+1,color,ori_color)
            dfs(i,j-1,color,ori_color)

            image[i][j] = color

            return 
        
        dfs(sr,sc,color,image[sr][sc])
        return image

