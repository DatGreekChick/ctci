# 4.7: Build Order

import collections


def construct_graph(dependencies: list):
    graph = collections.defaultdict(set)

    for d, p in dependencies:
        graph[p].add(d)

    return graph


def dfs(graph, project, stack, visited):
    for dependency in graph[project]:
        if dependency not in visited:
            dfs(graph, dependency, stack, visited)
            visited.add(dependency)

        if dependency not in stack:
            stack.append(dependency)

    stack.append(project)
    visited.add(project)


def create_order(order: list, graph: dict, pending: set):
    while pending:
        constructed = False

        for project in list(pending):
            deps = graph[project]

            if not pending.intersection(deps):
                order.append(project)
                pending.remove(project)
                constructed = True

        if not constructed:
            raise Exception("No valid build order exists")


def build_order(projects: list, dependencies: list):
    graph = construct_graph(dependencies)
    pending = set(projects)
    order = []
    create_order(order, graph, pending)

    return order


p = ["a", "b", "c", "d", "e", "f"]
d = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
print(build_order(p, d))  # ['f', 'e', 'a', 'b', 'd', 'c']]
print(build_order(["a", "b"], [("a", "b"), ("b", "a")]))  # Error
