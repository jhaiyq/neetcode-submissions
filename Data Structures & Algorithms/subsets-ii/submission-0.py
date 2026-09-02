class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        nums.sort()

        def backtrack(i, cur_set):
            
            # no condition on subsets
            res.append(cur_set[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                cur_set.append(nums[j])
                backtrack(j+1,cur_set)
                cur_set.pop()

        backtrack(0,[])
        return res