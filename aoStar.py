class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}

    def applyAOStar(self):
        self.aoStar(self.start, False)

    def getNeighbors(self, v):
        return self.graph.get(v, '')

    def getStatus(self, v):
        return self.status.get(v, 0)

    def setStatus(self, v, val):
        self.status[v] = val

    def getHeuristicNodeValue(self, n):
        return self.H.get(n, 0)

    def setHeuristicNodeValue(self, n, value):
        self.H[n] = value

    def printSolution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinimumCostChildNodes(self, v):
        minimumCost = 0
        costToChildNodeListDict = {} # to store cost of reaching child node
        costToChildNodeListDict[minimumCost] = [] #cost to child node dict initialize empty list 
        flag = True
        for nodeInfoTupleList in self.getNeighbors(v): #get the neighbors if it has "and" nodes then two tuples will be got 
            cost = 0
            nodeList = [] #to store the list of nodes
            for c, weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight #update cost with previous cost of and node with other and node if present
                nodeList.append(c)#append the node

            if flag == True:
                minimumCost = cost #update minimum cost 
                costToChildNodeListDict[minimumCost] = nodeList
                flag = False #so that next neighbor node will not come to this "if" loop
            else:
                if minimumCost > cost: #checks if previous minimum cost is greater then update it 
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList #update costtochild node dict

        return minimumCost, costToChildNodeListDict[minimumCost] 

    def aoStar(self, v, backTracking):
        print("HEURISTIC VALUES :", self.H) 
        print("SOLUTION GRAPH :", self.solutionGraph) #graph after previous iteration
        print("PROCESSING NODE :", v) #current processing node
        print("-----------------------------------------------------------------------------------------")

        if self.getStatus(v) >= 0: #for last node it will be -1 so
            minimumCost, childNodeList = self.computeMinimumCostChildNodes(v) # min cost and childnodelist of d for this eg for 1st iteration
            self.setHeuristicNodeValue(v, minimumCost)#setting the 1st node value
            self.setStatus(v, len(childNodeList))#setting the len of child node to status[v] ie for A in 1st iteration 

            solved = True
            for childNode in childNodeList: #
                self.parent[childNode] = v # set A as parent in 1st iteration
                if self.getStatus(childNode) != -1: #if it is not last node
                    solved = solved & False #set solved status to false

            if solved == True: #if it is true then solved so 
                self.setStatus(v, -1) # set the node status to -1 to show it is solved
                self.solutionGraph[v] = childNodeList #update solution graph child node list

            if v != self.start: #if node is not start node then call aostart algo for the node with its parent as argument 
                self.aoStar(self.parent[v], True)

            if backTracking == False:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)


h2 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph2 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}
G2 = Graph(graph2, h2, 'A')
G2.applyAOStar()
G2.printSolution()
