# 3.3: Stack of Plates

from stack import Node

# Runtime: O(1) - Space: O(1)
class StackInfo:
    def __init__(self):
        self.capacity = 3
        self.size = 0
        self.top = None


class SetOfStacks:
    def __init__(self):
        self.stacks = []

    def print(self):
        for idx, stack in enumerate(self.stacks):
            print(
                f"stack # {idx}: top: {stack.top.value} | stack size: {stack.size}"
            )

    def push(self, value):
        new_top = Node(value)
        info = self.stacks[-1] if self.stacks else StackInfo()

        if info.size < info.capacity:
            new_top.next = info.top
            info.size += 1
            info.top = new_top
        else:
            info = StackInfo()
            info.size += 1
            info.top = new_top
            self.stacks.append(info)

        if not self.stacks:
            self.stacks.append(info)

    def pop(self):
        info = self.stacks[-1]
        info.size -= 1
        item = info.top

        if info.top.next:
            info.top = info.top.next
        else:
            self.stacks.pop()

        return item


stack = SetOfStacks()
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(6)
stack.push(1)

stack.print()
print("popped:", stack.pop().value)
stack.print()
print("popped:", stack.pop().value)
stack.print()
print("popped:", stack.pop().value)
stack.print()
print("popped:", stack.pop().value)
stack.print()
print("popped:", stack.pop().value)
stack.print()
