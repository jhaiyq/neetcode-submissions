class Solution:

    def ceil(n):
        return -(-n // 1) 


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def binary_search(l, r):
            if l > r:
                return l   # reached minimum bananas
            
            k = (l + r) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                return binary_search(l, k - 1)   # try less bananas
            else:
                return binary_search(k + 1, r)   # try more bananas
        
        return binary_search(1, max(piles))