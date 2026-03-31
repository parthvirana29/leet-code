class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.max_limit = maxNumbers
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if self.available:
            return self.available.pop()
        return -1
    

    def check(self, number: int) -> bool:
        if number in self.available:
            return True
        return False
        

    def release(self, number: int) -> None:
        if number in self.available:
            return
        self.available.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)