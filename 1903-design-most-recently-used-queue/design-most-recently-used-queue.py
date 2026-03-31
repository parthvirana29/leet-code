class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MRUQueue:
    def __init__(self, n: int):
        self.head = Node(-1)  # Dummy head
        self.tail = Node(-2)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Build initial queue [1, 2, 3, ..., n]
        prev_node = self.head
        for i in range(1, n + 1):
            curr = Node(i)
            curr.prev = prev_node
            curr.next = self.tail
            prev_node.next = curr
            self.tail.prev = curr
            prev_node = curr
    
    def get_kth_node(self, k):
        """Get the k-th node (1-indexed)"""
        curr = self.head.next
        for _ in range(k - 1):
            curr = curr.next
        return curr
    
    def remove_node(self, node):
        """Remove node from its current position"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def append_to_end(self, node):
        """Append node to the end (before tail)"""
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
    
    def fetch(self, k: int) -> int:
        # Get the k-th node
        node = self.get_kth_node(k)
        val = node.val
        
        # Remove it from current position
        self.remove_node(node)
        
        # Append to end
        self.append_to_end(node)
        
        return val