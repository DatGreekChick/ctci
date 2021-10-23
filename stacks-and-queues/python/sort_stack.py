# 3.5: Sort Stack

from stack import Stack

# Runtime: O(n^2) - Space: O(n)
def sort_stack(stack: Stack) -> Stack:
    r = Stack()

    while not stack.is_empty():
        tmp = stack.pop()

        while not r.is_empty() and r.peek() > tmp:
            stack.push(r.pop())

        r.push(tmp)

    while not r.is_empty():
        stack.push(r.pop())

    return stack


s = Stack()
s.push(9)
s.push(1)
s.push(2)
s.push(7)
s.push(4)

sorted_stack = sort_stack(s)
curr = sorted_stack.top
while curr:
    print(curr.value)
    curr = curr.next
