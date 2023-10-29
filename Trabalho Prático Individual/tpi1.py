#STUDENT NAME: Tomás Sousa Fonseca
#STUDENT NUMBER: 107245

#DISCUSSED TPI-1 WITH: (names and numbers):


from tree_search import *

class OrderDelivery(SearchDomain):

    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
        # ANY NEEDED CODE CAN BE ADDED HERE

    def actions(self,state):
        city = state[0]
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==city):
                actlist += [(C1,C2)]
            elif (C2==city):
               actlist += [(C2,C1)]
        return actlist 

    def result(self,state,action):
        #IMPLEMENT HERE
        current_city = state[0]
        next_city = action[1] if action[0] == current_city else action[0]
        # Assuming the state is a tuple where the first element is the current city
        return (next_city,)

    def satisfies(self, state, goal):
        #IMPLEMENT HERE
        return state[0] in goal

    def cost(self, state, action):
        #IMPLEMENT HERE
        for (C1, C2, D) in self.connections:
            if (C1, C2) == action or (C2, C1) == action:
                return D
        return float('inf')  # if action not found, return infinity

    def heuristic(self, state, goal):
        #IMPLEMENT HERE
        x1, y1 = self.coordinates[state]
        x2, y2 = self.coordinates[goal]
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


 
class MyNode(SearchNode):

    def __init__(self,state,parent,arg3=None,arg4=None,arg5=None,arg6=None):
        super().__init__(state,parent)
        #ADD HERE ANY CODE YOU NEED
        self.depth = 0
        self.cost = 0
        self.heuristic = 0
        self.eval = 0
        self.marked_for_deletion = False
        self.children = []

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',maxsize=None):
        super().__init__(problem,strategy)
        #ADD HERE ANY CODE YOU NEED
        self.maxsize = maxsize

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        self.open_nodes += lnewnodes
        self.open_nodes.sort(key=lambda node: (node.eval, node.state))


    def search2(self):
        #IMPLEMENT HERE
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if node.parent == None:
                node.depth = 0
                node.cost = 0
                node.heuristic = 0
                node.eval = 0
                node.children = []
                node.marked_for_deletion = False

            if self.problem.goal_test(node.state):
                self.solution = node
                self.terminals = len(self.open_nodes)+1
                return self.get_path(node)
            self.non_terminals += 1
            self.lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                self.newstate = self.problem.domain.result(node.state,a)
                if self.newstate not in self.get_path(node):
                    self.newnode = MyNode(self.newstate,node)
                    self.newnode.depth = node.depth + 1
                    self.newnode.cost = node.cost + self.problem.domain.cost(node.state,a)
                    self.newnode.heuristic = self.problem.domain.heuristic(self.newstate,self.problem.goal)
                    self.newnode.eval = self.newnode.cost + self.newnode.heuristic
                    self.lnewnodes.append(self.newnode)
                    node.children.append(self.newnode)
            self.add_to_open(self.lnewnodes)
            self.tree_size = len(self.open_nodes) + self.non_terminals
            if self.strategy == 'A*' and self.maxsize is not None and self.tree_size > self.maxsize:
                self.manage_memory()
        return None        


    def manage_memory(self):
        #IMPLEMENT HERE
        while self.tree_size > self.maxsize:
            reversed_list = self.open_nodes[::-1]
            for node in reversed_list:
                if node.marked_for_deletion == False:
                    node.marked_for_deletion = True
                    if self.is_children_marked(node):
                        for child in node.parent.children:
                            self.open_nodes.remove(child)
                            self.non_terminals -= 1
                        parent = node.parent
                        min_eval = 0
                        for child in parent.children:
                            if child.eval < min_eval:
                                min_eval = child.eval
                        parent.eval = min_eval
                        self.open_nodes.append(parent)
                        self.non_terminals += 1
                        self.open_nodes.remove(node)
                    self.tree_size = len(self.open_nodes) + self.non_terminals

    # if needed, auxiliary methods can be added here

    def is_children_marked(self, node):
        for child in node.parent.children:
            if not child.marked_for_deletion:
                return False
        return True
    
def orderdelivery_search(domain,city,targetcities,strategy='breadth',maxsize=None):
    #IMPLEMENT HERE
    pass
 


# If needed, auxiliary functions can be added here



