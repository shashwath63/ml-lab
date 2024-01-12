def aStarAlgo(start_node,stop_node):
    open_set=set(start_node)#set of open nodes
    closed_set=set()#set of closed nodes
    g={} #store distance from starting node
    parents={} #parents contains an adjacency map of all nodes
    g[start_node]=0
    parents[start_node]=start_node
    while len(open_set) > 0:
        n=None
        for v in open_set:
            if n==None or g[v]+heuristic(v)< g[n]+heuristic(n):
                n=v
        if n==stop_node or Graph_nodes[n]==None:
            pass
        else:
            for (m,weight) in get_neighbors(n):
                if m not in open_set or m not in closed_set:
                    open_set.add(m)     #add that node to open set
                    parents[m]=n        #update parent of the node to be previous node
                    g[m]=g[n]+weight    #update distance for node to be g[n]:ie distance to that node  + weight
                else:
                    if g[m] > g[n] + weight: #distance from n node is less than previous m distance 
                        g[m] = g[n] + weight 
                        parents[m]=n
                        if m in closed_set: # if its neighbours are visited remove them and add to open set
                            closed_set.remove(m)
                            open_set.add(m)
        if n==None :
            print('path does not exist')
            return None
        if n==stop_node:
            path=[]     #empty list
            while parents[n]!=n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print("path found:{}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)


def heuristic(n):
    H_dist = {           #dictionary
        'A':10,
        'B':8,
        'C':5,
        'D':7,
        'E':3,
        'F':6,
        'G':5,
        'H':3,
        'I':1,
        'J':0
    }
    return H_dist[n]
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else: 
        return None
Graph_nodes={           #dictionary of LIST
    'A':[('B',6),('F',3)], #LIST OF TUPLES
    'B':[('C',3),('D',2)], 
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}
aStarAlgo('A','J')