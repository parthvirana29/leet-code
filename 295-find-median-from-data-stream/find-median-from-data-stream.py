import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
   
    def addNum(self, num: int) -> None:
        # however u can't simply print
        heapq.heappush(self.max_heap, -num)
        len_difference = len(self.max_heap) - len(self.min_heap)
        if (len(self.max_heap) > 1 + len(self.min_heap) or (self.min_heap and -self.max_heap[0] > self.min_heap[0])):
            # find the max in max_heap - O(1)
            # also invert the number
            max_in_max_heap = -self.max_heap[0]
            # remove the largest value from max_heap - O(log n)
            heapq.heappop(self.max_heap)
            # add the largest value from max_heap - O(log n)
            heapq.heappush(self.min_heap, max_in_max_heap)
        if (len(self.min_heap) > 1 + len(self.max_heap)):
            min_in_min_heap = -1 * self.min_heap[0]
            # remove the largest value from max_heap - O(log n)
            heapq.heappop(self.min_heap)
            # add the largest value from max_heap - O(log n)
            heapq.heappush(self.max_heap, min_in_min_heap)

    def findMedian(self) -> float:
        # find len
        n_max = len(self.max_heap)
        n_min = len(self.min_heap)
        total = n_max + n_min
        median = 0
        if (total) % 2 == 0:
            median = (-self.max_heap[0] + self.min_heap[0])/2
        else:
            if (n_max > n_min):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        return median

            

        

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()