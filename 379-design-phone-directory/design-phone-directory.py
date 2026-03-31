class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.max_limit = maxNumbers
        self.used = set()
        self.un_used = set([i for i in range(self.max_limit)])
        print(self.un_used)

    def get(self) -> int:
        if self.un_used:
            temp = self.un_used.pop()
            self.used.add(temp)
            return temp
        return -1
    

    def check(self, number: int) -> bool:
        if number in self.un_used:
            return True
        return False
        

    def release(self, number: int) -> None:
        if number not in self.used:
            return
        self.used.remove(number)
        self.un_used.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)