from collections import deque
class Logger:

    def __init__(self):
        self.queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # anything older than 10 seconds drop it
        while (self.queue and  timestamp - 10 >= self.queue[0][0] ):
            self.queue.popleft()
        for time, old_msg in self.queue:
            if message == old_msg:
                return False
        self.queue.append([timestamp, message])
        return True


        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)