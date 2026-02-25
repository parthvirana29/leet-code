from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.queue:
                self.queue.remove(key)
                self.queue.append(key)
            return self.cache[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            return
        newSize = self.size + 1
        if newSize > self.capacity:
            key2 = self.queue.popleft()
            self.cache.pop(key2)
            self.cache[key] = value
            self.queue.append(key)
            return

        self.size += 1
        self.queue.append(key)
        self.cache[key] = value

        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)