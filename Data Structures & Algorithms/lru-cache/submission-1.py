class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity: int):
        self.cap = capacity
        self.maps = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def pop(self, node):
        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if key in self.maps:
            self.pop(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.pop(self.maps[key])
        self.maps[key] = Node(key, value)
        self.insert(self.maps[key])

        if self.cap < len(self.maps):
            lru = self.left.next
            self.pop(lru)
            del self.maps[lru.key]

