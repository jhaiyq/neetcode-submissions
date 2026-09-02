class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #[1,2,2,4,5,6,9] target = 8
        candidates.sort()

        res = []

        def dfs(i, subset, count):
            if count == target:
                res.append(subset[:])
                return

            if i == len(candidates) or count > target:
                return
            
            cur_val = candidates[i]
            subset.append(cur_val)
            dfs(i+1,subset,count+cur_val)
            subset.pop()

            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:    
                i += 1
            dfs(i+1,subset, count)
            return
        
        dfs(0,[],0)
        return res


