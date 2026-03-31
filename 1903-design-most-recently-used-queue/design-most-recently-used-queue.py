class MRUQueue:

    def __init__(self, n: int):
        self.q = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        val = self.q.pop(k - 1)   # remove k-th element
        self.q.append(val)        # move it to the end
        return val
