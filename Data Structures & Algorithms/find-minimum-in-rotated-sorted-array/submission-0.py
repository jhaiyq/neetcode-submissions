class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0,len(nums)-1
        mini = nums[0]

        while l <= r:

            if nums[l] < nums[r]:
                mini = min(mini,nums[l])
                break
            
            m = (l+r)//2
            mini = min(mini,nums[m])
            if nums[m] < nums[l]:
                r = m-1
            else:
                l = m +1
        return mini