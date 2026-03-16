
class HitCounter:

    def __init__(self):
        self.mono_stack = []
        self.l = 0
        

    def hit(self, timestamp: int) -> None:
        self.mono_stack.append(timestamp)
        # self.freq[timestamp] = self.freq.get(timestamp, 0 ) + 1
        
            
        while self.l < len(self.mono_stack) and self.mono_stack[self.l] <= timestamp - 300:
            self.l += 1
        print(self.mono_stack)
        print(self.l)

    def getHits(self, timestamp: int) -> int:
        while self.l < len(self.mono_stack) and self.mono_stack[self.l] <= timestamp - 300:
            self.l += 1
        print(self.mono_stack)
        print(self.l)
        return len(self.mono_stack) - self.l
    
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)