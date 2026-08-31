class DLLNode:
    def __init__(self, key, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.nodes = {}
        self.head = None
        self.tail = None
        
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.addToFront(self.nodes[key])
        return self.nodes[key].val
    def addToFront(self, node):
        if node is self.head:
            return
        if node.key in self.nodes:

            if node.prev:
                node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
    
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def evict(self):
        
        del self.nodes[self.tail.key]
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.count -= 1
        

    def put(self, key: int, value: int) -> None:

        if key in self.nodes:
            self.nodes[key].val = value
            self.addToFront(self.nodes[key])
            return
        if self.count == self.capacity:
            self.evict()

        current = DLLNode(key, value, None, self.head)
        self.addToFront(current)
        self.nodes[key] = current
        self.count += 1
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
