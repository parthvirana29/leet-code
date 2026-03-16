from collections import deque
class HitCounter:

    def __init__(self):
        self.mono_q = deque()
        self.total = 0
        

    def hit(self, timestamp: int) -> None:
        prev = 0
        if self.mono_q:
            prev_ts, freq = self.mono_q[-1]
            if (timestamp == prev_ts):
                self.mono_q[-1][1] += 1
                self.total += 1
                return
        self.mono_q.append([timestamp,1])
        self.total += 1
    

    def getHits(self, timestamp: int) -> int:
        while self.mono_q and self.mono_q[0][0] <= timestamp - 300:
            ts, freq = self.mono_q.popleft()
            self.total -= freq
        return self.total
    
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)