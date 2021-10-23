# 3.1: Three in One

from sq_exceptions import StackEmptyException, StackFullException


class FixedMultiStack:
    def __init__(self, capacity):
        self.num_stacks = 3
        self.capacity = capacity
        self.values = [0] * (self.capacity * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    # Runtime: O(1) - Space: O(1)
    def push(self, stack_num: int, item: int) -> None:
        if self.is_full(stack_num):
            raise StackFullException("Stack is full!")

        self.sizes[stack_num] += 1
        idx = self.index_of_top(stack_num)
        self.values[idx] = item

    # Runtime: O(1) - Space: O(1)
    def pop(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            raise StackEmptyException("Stack has nothing to pop!")

        idx = self.index_of_top(stack_num)
        item = self.values[idx]
        self.values[idx] = 0
        self.sizes[stack_num] -= 1

        return item

    # Runtime: O(1) - Space: O(1)
    def peek(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            raise StackEmptyException("Stack is empty. Nothing to peek at!")

        idx = self.index_of_top(stack_num)
        return self.values[idx]

    # Runtime: O(1) - Space: O(1)
    def is_empty(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == 0

    # Runtime: O(1) - Space: O(1)
    def is_full(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == self.capacity

    # Runtime: O(1) - Space: O(1)
    def size(self, stack_num: int) -> int:
        return self.sizes[stack_num]

    # Runtime: O(1) - Space: O(1)
    def index_of_top(self, stack_num: int) -> int:
        offset = stack_num * self.capacity
        size = self.sizes[stack_num]
        return offset + size - 1


stack = FixedMultiStack(3)
stack.push(0, 5)
print(stack.peek(0))
stack.push(0, 3)
print(stack.pop(0))
print(stack.is_empty(0))
print(stack.is_full(0))
stack.push(0, 1)
stack.push(0, 2)
print(stack.size(0))
print(stack.is_empty(0))
print(stack.is_full(0))
