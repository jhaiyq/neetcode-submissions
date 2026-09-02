class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(ind, path):
            # Base Case 
            if len(path) == k:
                result.append(path[:])

            for i in range(ind, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()

        backtrack(1,[])  

        return result

