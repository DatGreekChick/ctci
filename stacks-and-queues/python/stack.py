from sq_exceptions import EmptyStackException


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Nothing to pop.")

        item = self.top
        self.top = self.top.next
        self.size -= 1
        return item.value

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise EmptyStackException("Nothing to peek.")

        return self.top.value
