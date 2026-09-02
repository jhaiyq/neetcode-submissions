class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
            
        count = total = 0
        hashm = {0: 1}

        for num in nums:
            total += num
            diff = total - k

            count += hashm.get(diff, 0)

            hashm[total] = 1 + hashm.get(total,0)
        
        return count