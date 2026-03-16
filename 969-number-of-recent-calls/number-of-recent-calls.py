from collections import Counter
class RecentCounter:

    def __init__(self):
        self.log = []
        self.l = 0

    def ping(self, t: int) -> int:
        self.log.append(t)
        num_requests = 0
        r = len(self.log)
        while self.log[self.l] < t - 3000:
            self.l += 1
        return r - self.l




            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)