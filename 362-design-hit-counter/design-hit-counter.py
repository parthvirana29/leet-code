from collections import deque
class HitCounter:

    def __init__(self):
        self.mono_q = deque()
        

    def hit(self, timestamp: int) -> None:
        self.mono_q.append(timestamp)
        # self.freq[timestamp] = self.freq.get(timestamp, 0 ) + 1
        
            
        while self.mono_q and self.mono_q[0] <= timestamp - 300:
            self.mono_q.popleft()
        print(self.mono_q)

    def getHits(self, timestamp: int) -> int:
        while self.mono_q and self.mono_q[0] <= timestamp - 300:
            self.mono_q.popleft()
        print(self.mono_q)
        return len(self.mono_q) 
    
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)