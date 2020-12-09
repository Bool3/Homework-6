from search import Problem, Node

class BucharestProblem(Problem):

    # I updated your map so that all the cities are keys
    romania_map = {
        "Arad"      :  {"Zerind" : 75, "Timisoara" : 118, "Sibiu" : 140},
        "Sibiu"     :  {"Arad" : 140, "Oradea" : 151, "Rimnicu" : 80, "Fagaras" : 99},
        "Zerind"    :  {"Arad" : 75, "Oradea": 71},
        "Timisoara" :  {"Arad" : 118, "Lugoj" : 111},
        "Mehadia"   :  {"Lugoj" : 70, "Drobeta" : 75},
        "Bucharest" :  {"Urziceni" : 85, "Pitesti" : 101, "Giurgiu" : 90, "Fagaras" : 211},
        "Craiova"   :  {"Drobeta" : 120, "Rimnicu" : 146, "Pitesti" : 138},
        "Drobeta"   :  {"Mehadia" : 75, "Craiova" : 120},
        "Fagaras"   :  {"Sibiu" : 99, "Bucharest" : 211},
        "Lugoj"     :  {"Timisoara" : 111, "Mehadia" : 70},
        "Oradea"    :  {"Zerind" : 71, "Sibiu" : 151},
        "Pitesti"   :  {"Rimnicu" : 97, "Craiova" : 138, "Bucharest" : 101},
        "Rimnicu"   :  {"Sibiu" : 80, "Pitesti" : 97},
        "Giurgiu"   :  {"Bucharest" : 90},
        "Urziceni"  :  {"Bucharest" : 85}
        }


    def __init__(self,start="Arad",goal="Bucharest"):
        super().__init__(start,goal)


    def actions(self, state):
        ret = []

        for value_city, _ in self.romania_map[state].items():
            ret.append("GO_" + value_city)
            
        return ret


    def result(self, state, action):
        #an action is just (go) to the state specifed in the action
        #actions are state names prefixed with 'GO_'
        return action[3:]
    

    def path_cost(self, c, state1, action, state2):
        return c + self.romania_map[state1][state2]


if __name__ == '__main__':
    from bfs import uniform_cost_search, breadth_first_search
    
    print("")
    print("---BREADTH FIRST SEARCH: ROMANIA---")
    solution_node = breadth_first_search(BucharestProblem())
    if type(solution_node) == Node:
        solution = solution_node.solution()
        
        print(f"Solution Path: {solution}")
        print(f"Distance Traveled: {solution_node.path_cost}")
    else:
        print(solution_node)
    print("")
    
    print("---UNIFORM COST SEARCH: ROMANIA---")
    solution_node = uniform_cost_search(BucharestProblem())
    if type(solution_node) == Node:
        solution = solution_node.solution()

        print(f"Solution Path: {solution}")
        print(f"Distance Traveled: {solution_node.path_cost}")
    else:
        print(solution_node)
    print("")