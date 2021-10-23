# 3.4: Queue via Stacks

from stack import Stack


class MyQueue:
    def __init__(self):
        self.oldest_stack = Stack()
        self.newest_stack = Stack()

    def size(self):
        return self.oldest_stack.size + self.newest_stack.size

    def add(self, value):
        self.newest_stack.push(value)

    def peek(self):
        self.shift_stacks()
        return self.oldest_stack.peek()

    def remove(self):
        self.shift_stacks()
        return self.oldest_stack.pop()

    def shift_stacks(self):
        if self.oldest_stack.is_empty():
            while not self.newest_stack.is_empty():
                self.oldest_stack.push(self.newest_stack.pop())


queue = MyQueue()
queue.add(5)
print("peek:", queue.peek())
print("size:", queue.size())
queue.add(2)
print("peek:", queue.peek())
print("size:", queue.size())
print("remove:", queue.remove())
print("size:", queue.size())
print("peek:", queue.peek())
