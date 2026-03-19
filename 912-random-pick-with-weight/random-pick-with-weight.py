import random
class Solution:

    def __init__(self, w: List[int]):
        # 3, 4, 1, 2
        # P(3) = 3/10
        # P(4) = 4/10 
        # P(1) = 1/10
        # P(2) = 2/10
        # So range has to be sum of all the weights.
        # Now I need to determine the inner range that is assigned to each number
        # 3, *4* 7, 8, 10
        # 1,2,3 = 3
        # 4,5,6,7 = 4
        # 8 = 1
        # 9, 10 = 2

        self.prefix_sum = [w[0]]
        for i in range(1,len(w)):
            self.prefix_sum.append(self.prefix_sum[i-1] + w[i])
        # print(prefix_sum)
    def pickIndex(self) -> int:
        val = random.uniform(0, self.prefix_sum[-1])
        # find the val in prefix sum
        l, r = 0, len(self.prefix_sum)
        while (l < r):
            mid = (l + r) //2
            mid_val = self.prefix_sum[mid]
            if (val < mid_val):
                r = mid
            elif (val > mid_val):
                l = mid + 1
            else:
                return l
  
        return l
            


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()