from search import Problem, Node

class BucharestProblem(Problem):

    romania_map = {
        "Arad"      :  {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
        "Bucharest" :  {"Urziceni": 85, "Pitesti": 101, "Giurgiu": 90, "Fagaras": 211},
        "Craiova"   :  {"Drobeta": 120, "Rimnicu": 146, "Pitesti": 138},
        "Drobeta"   :  {"Mehadia": 75, "Craiova": 120},
        "Eforie"    :  {"Hirsova": 86},
        "Fagaras"   :  {"Sibiu": 99, "Bucharest": 211},
        "Giurgiu"   :  {"Buchareset": 90},
        "Hirsova"   :  {"Urziceni": 98, "Eforie": 86},
        "Iasi"      :  {"Vaslui": 92, "Neamt": 87},
        "Lugoj"     :  {"Timisoara": 111, "Mehadia": 70},
        "Mehadia"   :  {"Lugoj", 70, "Drobeta": 75},
        "Neamt"     :  {"Iasi": 87},
        "Oradea"    :  {"Zerind": 71, "Sibiu": 151},
        "Pitesti"   :  {"Rimnicu": 97, "Bucharest": 101},
        "Rimnicu"   :  {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
        "Sibiu"     :  {"Rimnicu": 80, "Fagaras": 99, "Oradea": 151, "Arad": 140 },
        "Timisoara" :  {"Arad": 118, "Lugoj": 111},
        "Urziceni"  :  {"Vaslui": 142, "Bucharest": 85, "Hirsova": 98},
        "Vaslui"    :  {"Iasi": 92, "Urziceni": 142},
        "Zerind"    :  {"Oradea": 71, "Arad": 75}
        }
    
    romania_straight_line_distance = {
        "Arad"      :  366,
        "Bucharest" :  0,
        "Craiova"   :  160,
        "Drobeta"   :  242,
        "Eforie"    :  161,
        "Fagaras"   :  176,
        "Giurgiu"   :  77,
        "Hirsova"   :  151,
        "Iasi"      :  226,
        "Lugoj"     :  244,
        "Mehadia"   :  241,
        "Neamt"     :  234,
        "Oradea"    :  380,
        "Pitesti"   :  100,
        "Rimnicu"   :  193,
        "Sibiu"     :  253,
        "Timisoara" :  329,
        "Urziceni"  :  80,
        "Vaslui"    :  199,
        "Zerind"    :  374
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