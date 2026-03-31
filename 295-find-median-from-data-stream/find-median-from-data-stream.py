import heapq

class MedianFinder:

    def __init__(self):
        self.low_nums = [] # negative values because I want highest value
        self.high_nums = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low_nums, -1*num)
        if len(self.low_nums) > 1 + len(self.high_nums) or (self.high_nums and self.high_nums[0] < (-1*self.low_nums[0])):
            elem = -1*heapq.heappop(self.low_nums)
            heapq.heappush(self.high_nums, elem)
        if len(self.high_nums) > 1 + len(self.low_nums):
            elem = heapq.heappop(self.high_nums)
            heapq.heappush(self.low_nums, -1*elem)

    def findMedian(self) -> float:
        n_low = len(self.low_nums)
        n_high = len(self.high_nums)
        total = n_low + n_high
        if (total % 2 == 0 and self.low_nums and self.high_nums):
            return ((-1*self.low_nums[0]) + self.high_nums[0])/2
        elif (total % 2 != 0 ):
            if (n_low > n_high):
                return -1*self.low_nums[0]
            return self.high_nums[0]
        return 0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()