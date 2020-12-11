import random
from collections import deque
import copy
from search import Problem, Node, NodePriorityQueue
from romania import BucharestProblem

# best first search
def sarkissian_hw6_1(problem):

    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    frontier = deque([node])
    visited = [problem.initial]

    while len(frontier) > 0:

        node = frontier.pop()

        for child in node.expand(problem):
            frontier.append(child)

        for child in random_children:

            if problem.goal_test(child.state):
                print(f"Nodes Visited: {len(visited)}")
                return child

            if child.state not in visited:
                visited.append(child.state)
                frontier.append(child)
                sarkissian_hw6_1(BucharestProblem(child.state))

    return "FAILED"
