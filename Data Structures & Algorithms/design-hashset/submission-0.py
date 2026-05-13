class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [Node(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.data == key:
                return
            cur = cur.next

        cur.next = Node(key)
        
    def remove(self, key: int) -> None:
        tmp = self.set[key % len(self.set)]
        while tmp.next:
            if tmp.next.data == key:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next
                
    def contains(self, key: int) -> bool:
        tmp = self.set[key % len(self.set)]
        while tmp.next:
            if tmp.next.data == key:
                return True
            tmp = tmp.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)