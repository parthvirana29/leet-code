import random
class Solution:

    def __init__(self, w: List[int]):
        self.arr = [w[0]]
        for i in range(1,len(w)):
            self.arr.append(w[i] + self.arr[i-1])
        print(self.arr)

    def pickIndex(self) -> int:
        n = len(self.arr)
        pick = random.uniform(0,self.arr[-1])
        print(pick)
        l, r = 0, n
        while (l < r):
            mid = (l + r) //2
            if (pick > self.arr[mid]):
                l = mid + 1
            elif (pick < self.arr[mid]):
                r = mid
            else:
                return l
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()