class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, cur_sub, count):
           
            # if count reaches target
            if  count == target:
                res.append(cur_sub[:])
                return

            if i >= len(nums) or count > target:
                return

            cur_sub.append(nums[i])
            dfs(i, cur_sub, count + nums[i])
            cur_sub.pop()
            dfs(i+1, cur_sub, count)
        
        dfs(0,[],0)
        return res
