from collections import deque

# my first approach was to use deque but it was slow because I kept updating the storage. PLEASE READ THE PROBLEM CUTIE
class Logger:

    def __init__(self):
        self.msg_log = {}
        self.RATE_LIMIT = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # anything older than 10 seconds drop it
        if message in self.msg_log and  timestamp - self.msg_log[message] < self.RATE_LIMIT:
            return False

        self.msg_log[message] = timestamp
        return True



        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)