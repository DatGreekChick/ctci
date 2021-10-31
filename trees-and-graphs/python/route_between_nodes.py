# 4.1: Route Between Nodes

from queue import Queue

from graphs import Status


class Node:
    def __init__(self, value):
        self.value = value
        self.state = Status.UNVISITED
        self.adjacent = []


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, node: Node) -> None:
        self.nodes.append(node)


def route_between_nodes(graph: Graph, start: Node, end: Node) -> bool:
    if start == end:
        return True

    q = Queue()

    start.state = Status.VISITING
    q.put(start)
    unvisited = None

    while not q.empty():
        unvisited = q.get()

        if unvisited:
            for vertex in unvisited.adjacent:
                if vertex.state == Status.UNVISITED:
                    if vertex == end:
                        return True

                    vertex.state = Status.VISITING
                    q.put(vertex)

            unvisited.state = Status.VISITED

    return False


four = Node(4)
five = Node(5)
six = Node(6)
four.adjacent = [six]
six.adjacent = [five]
five.adjacent = [four]

zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
zero.adjacent = [one]
one.adjacent = [two]
two.adjacent = [zero, three]
three.adjacent = [two]

g = Graph()
g.add(four)
g.add(five)
g.add(six)
g.add(zero)
g.add(one)
g.add(two)
g.add(three)

print(route_between_nodes(g, four, five))  # True
print(route_between_nodes(g, zero, one))  # True
print(route_between_nodes(g, three, two))  # True
print(route_between_nodes(g, two, three))  # False
print(route_between_nodes(g, four, zero))  # False
