from search import Problem, Node, NodePriorityQueue
from romania import BucharestProblem


# greedy search
def sarkissian_hw6_1(problem):

    node = Node(problem.initial)

    # heuristic function = the node's straight line distance to the goal node
    def h(_node):
        return problem.straight_line_distance(_node.state)

    frontier = NodePriorityQueue(h)
    frontier.push(node)
    visited = []

    while len(frontier) > 0:

        # pop a node out of the queue (this will always be the node with the lowest hueristic)
        node = frontier.pop()[1]  # NodePriorityQueue.pop() returns a tuple = (heuristic(node), node)
        visited.append(node.state)

        # if that node is the goal node, return the solution
        if problem.goal_test(node.state):
            
            print(f"Nodes Visited: {len(visited)}")
            print(f"Distance Traveled: {node.path_cost}")

            return [(n.state, h(n)) for n in node.path()]  # returns a list of 2-tuples (node.state, heuristic(node))

        # if that node isn't the goal node, add its children to the frontier if they haven't already been visited
        for child in node.expand(problem):
            if child.state not in visited:
                frontier.push(child)
                
    return "FAILED"


# A-star
def sarkissian_hw6_2(problem):

    node = Node(problem.initial)

    if problem.goal_test(node.state):
        return node

    # heuristic function = the node's straight line distance to the goal node + the node's path cost
    def h(_node):
        return problem.straight_line_distance(_node.state) + _node.path_cost

    frontier = NodePriorityQueue(h)
    frontier.push(node)
    visited = []

    while len(frontier) > 0:

        # pop a node out of the queue (this will always be the node with the lowest hueristic)
        node = frontier.pop()[1]  # NodePriorityQueue.pop() returns a tuple = (heuristic(node), node)
        visited.append(node.state)

        # if that node is the goal node, return the solution
        if problem.goal_test(node.state):

            print(f"Nodes Visited: {len(visited)}")
            print(f"Distance Traveled: {node.path_cost}")
            
            return [(n.state, h(n)) for n in node.path()]  # returns a list of 2-tuples (node.state, heuristic(node))

        # if that node isn't the goal node, add its children to the frontier if they haven't already been visited
        for child in node.expand(problem):
            if child.state not in visited:
                frontier.push(child)
                
    return "FAILED"