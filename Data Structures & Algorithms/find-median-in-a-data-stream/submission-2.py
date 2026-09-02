import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.len_max = 0
        self.minheap = []
        self.len_min = 0
        
    def addNum(self, num: int) -> None:
        diff = self.len_max - self.len_min
        if self.len_max == 0:
            heapq.heappush(self.maxheap, -num)
            self.len_max += 1
        elif diff == 0:
            # Must balance to the left
            if num < self.minheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                left = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -left)
                heapq.heappush(self.minheap, num)
            self.len_max += 1
        elif diff > 0:
            # Must balance to the right
            if num >= -self.maxheap[0]:
                heapq.heappush(self.minheap, num)
            if num < -self.maxheap[0]:
                right = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, right)
                heapq.heappush(self.maxheap, -num)
            self.len_min += 1

        
    def findMedian(self) -> float:
        diff = self.len_max - self.len_min

        if diff == 0:
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return -self.maxheap[0]

        
        