class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def remove(self, elem):
        prev = None
        curr = self.head

        if curr is not None and curr.data == elem:
            self.head = curr.next
            self.size -= 1
            return

        while curr:
            if curr.data == elem:
                prev.next = curr.next
                self.size -= 1
                return

            prev = curr
            curr = curr.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
