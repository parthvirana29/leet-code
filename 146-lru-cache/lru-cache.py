class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node
    
    # we don't have to do any error checking because of extra (-1,-1) node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # we don't have to do any error checking because of extra (-1,-1) node
    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1

        node = self.dictionary[key]
        self.remove(node)
        self.add(node)
        return node.val
    

    def put(self, key: int, value: int) -> None:
        if (key in self.dictionary):
            # remove old node if one exists
            old_node = self.dictionary[key]
            self.remove(old_node)
        # add a node with the key value towards the end and also keep track of it in the dictionary
        node = ListNode(key,value)
        self.add(node)
        self.dictionary[key] = node
        # check if we have gone past the capacity
        if (len(self.dictionary) > self.capacity):
            node_to_remove = self.head.next
            del self.dictionary[node_to_remove.key]
            self.remove(node_to_remove)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)