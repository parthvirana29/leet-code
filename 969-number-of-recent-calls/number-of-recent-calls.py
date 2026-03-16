from collections import Counter
class RecentCounter:

    def __init__(self):
        self.log = []

    def ping(self, t: int) -> int:
        self.log.append(t)
        num_requests = 0
        for i in range(len(self.log) - 1, -1 ,-1):
            if (self.log[i] < t - 3000):
                break
            num_requests += 1
        return num_requests


            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)