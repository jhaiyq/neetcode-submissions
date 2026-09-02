class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirc = [[1,0],[0,1],[-1,0],[0,-1]]  
        res = []
        ROWS, COLS  = len(board), len(board[0])

        def dfs(r,c, i):

            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c>= COLS:
                return False
            
            if word[i] != board[r][c] or board[r][c] == "#":
                return False

            temp = board[r][c]
            board[r][c] = "#"
            res = any(dfs(r + dr, c + dc, i + 1) for dr, dc in dirc)
            board[r][c] = temp
            return res
                
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False


