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

    def h(_node):
        return problem.straight_line_distance(_node.state)

    # frontier needs to be a priority queue based on the heuristic h(n) =  straight line distance to bucharest
    frontier = NodePriorityQueue(h)
    frontier.push(node)
    visited = [problem.initial]

    while len(frontier) > 0:

        node = frontier.pop()[1]  # the pop() returns a tuple = (hueristic(node), node)

        if problem.goal_test(node):
            print(f"Nodes Visited: {len(visited)}")
            return node

        for child in node.expand(problem):
            if child.state not in visited:
                frontier.push(child)
                visited.append(node.state)
                sarkissian_hw6_1(BucharestProblem(child.state))
                
    return "FAILED"


# A-Star
def sarkissian_hw6_2(problem):
    pass