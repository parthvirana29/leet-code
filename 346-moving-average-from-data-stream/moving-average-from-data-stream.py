from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.moving_avg = 0


    def next(self, val: int) -> float:
        n = len(self.q)
        self.q.append(val)
        if (n + 1 > self.size):
            get_rid_val = self.q.popleft()
            sub_avg = get_rid_val / (n)
            self.moving_avg -= sub_avg
            self.moving_avg += (val/n)
            return self.moving_avg
        base_sum = (self.moving_avg * n) + val
        self.moving_avg = base_sum / len(self.q)
        return self.moving_avg



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)