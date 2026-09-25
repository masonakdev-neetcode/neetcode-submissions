class Node:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        ptr = self.head
        for _ in range(index):
            ptr = ptr.nxt
        
        return ptr.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.nxt = self.head
            self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nxt = newNode
            self.tail = newNode
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False

        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                self.head = temp.nxt
                temp = None
            self.length -= 1
            return True
        

        ctr = 1
        prev = self.head
        curr = self.head.nxt
        while curr:
            nxt = curr.nxt
            if ctr == index:
                prev.nxt = nxt
                curr = None
                break
            prev = curr
            curr = nxt
            ctr += 1
        
        if index == self.length - 1:
            self.tail = prev

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.val)
            curr = curr.nxt
        return vals
