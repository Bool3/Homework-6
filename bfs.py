import random
from collections import deque
import copy
from search import Problem, Node, NodePriorityQueue


def breadth_first_search(problem):

    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    frontier = deque([node])
    visited = [problem.initial]

    while len(frontier) > 0:

        node = frontier.popleft()

        random_children = copy.copy(node.expand(problem))
        random.shuffle(random_children)

        for child in random_children:
            s = child.state

            if problem.goal_test(s):
                print(f"Nodes Visited: {len(visited)}")
                return child

            if s not in visited:
                visited.append(s)
                frontier.append(child)

    return "FAILED"


def uniform_cost_search(problem):

    node = Node(problem.initial)

    frontier = NodePriorityQueue()
    frontier.push(node)

    visited = []

    while True:

        if len(frontier.values) == 0:
            return "FAILED"

        node = frontier.pop()[1]

        if problem.goal_test(node.state):
            print(f"Nodes Visited: {len(visited)}")
            return node
        
        visited.append(node.state)

        for action in problem.actions(node.state):
            child = node.child_node(problem, action)

            if child.state not in visited or not frontier.does_contain(child):
                frontier.push(child)

            elif frontier.does_contain(child) and frontier.values[frontier.get_index(child)][0] > child.path_cost:
                frontier.update(child)

    return "FAILED"


def eight_puzzle_search(problem):

    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    frontier = deque([node])
    visited = set([hash(problem.initial)])

    while len(frontier) > 0:

        node = frontier.popleft()

        random_children = node.expand(problem)
        random.shuffle(random_children)

        for child in random_children:
            s = child.state

            if problem.goal_test(s):
                print(f"Nodes Visited: {len(visited)}")
                return child

            if s not in visited:
                visited.add(s)
                frontier.append(child)

    return "FAILED"