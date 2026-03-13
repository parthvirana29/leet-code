import random

class Solution:

    def __init__(self, w: List[int]):
        self.pos_integers = w
        self.prefix_sum = [w[0]]
        # start at correct index range (1, len(arr)). 1 is important
        for i in range(1,len(self.pos_integers)):
            self.prefix_sum.append(self.prefix_sum[-1] + self.pos_integers[i])
        
    def pickIndex(self) -> int:
        start = 0
        end = self.prefix_sum[-1]
        random_num = random.uniform(start, end)
        print(random_num)
        l, r = 0, len(self.prefix_sum)
        while (l < r):
            # 3.5 
            # 0, 1, 2, 3 
            # 1, 3, 6, 10
            mid = (l + r) // 2
            if (self.prefix_sum[mid] < random_num):
                # remember we don't move by l += 1 but l = mid + 1
                l = mid + 1
            elif self.prefix_sum[mid] > random_num:
                # r does not equal r-= 1 but r = mid.
                # this is why binary search is powerful each time it runs it cuts its area of iteration to half
                r = mid
          
        print("l: ", l, "r: ", r, "mid: ", mid )
        return l
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()