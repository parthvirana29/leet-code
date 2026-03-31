class MRUQueue:

    def __init__(self, n: int):
        self.nums = SortedList((v,v) for v in range(1,n+1)) # pos, value
        print(self.nums)

    def fetch(self, k: int) -> int:
        # doing k-1 because list is 0 indexed
        res = self.nums[k-1][1]
        last_pos = self.nums[-1][0]
        # delete current position
        del self.nums[k-1]
        # move it to end by updating the position value
        self.nums.add((last_pos+1, res))
        return res


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)