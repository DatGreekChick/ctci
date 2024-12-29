# 3.2: Stack Min

# Runtime: O(1) - Space: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.minimum = None


class Stack:
    def __init__(self):
        self.top = None
        self.minimum = None

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

        if not self.minimum:
            self.minimum = new_top
            return

        if value < self.minimum.value:
            new_top.minimum = self.minimum
            self.minimum = new_top
        else:
            new_top.minimum = self.minimum

    def pop(self):
        item = self.top
        self.minimum = self.top.minimum
        self.top = self.top.next
        return item

    def min(self):
        return self.minimum


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(6)
stack.push(1)

print("top:", stack.top.value)
print("min:", stack.min().value)
print("popped:", stack.pop().value)
print("top:", stack.top.value)
print("min:", stack.min().value)
print("popped:", stack.pop().value)
print("top:", stack.top.value)
print("min:", stack.min().value)
print("popped:", stack.pop().value)
print("top:", stack.top.value)
print("min:", stack.min().value)
print("popped:", stack.pop().value)
print("top:", stack.top.value)
print("min:", stack.min().value)
print("popped:", stack.pop().value)
