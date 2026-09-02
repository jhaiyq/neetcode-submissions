class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        steps = [ len(matrix[0]),  len(matrix) - 1]

        i,j, d_index = 0, -1, 0
        while steps[d_index & 1]:

            for k in range(steps[d_index & 1]):

                i += directions[d_index][0]
                j += directions[d_index][1]
                ans.append(matrix[i][j])

            steps[d_index & 1] -= 1
            d_index += 1
            d_index %= 4

        return ans