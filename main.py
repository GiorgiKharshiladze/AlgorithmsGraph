from graph import graph
import re


if __name__ == "__main__":
    

    """Reading file and building graph"""
    while True:
        filename = input("Enter Filename: ")         
        try:
            with open(filename) as file:
                data1 = file.read().rstrip()           
                data2 = re.split(r'[\n ' ' -]',data1) # parsing the input data file
                break
        except Exception:
            print ('This file does not exist. Try Again.')
    print ()
    
    g = graph() ## object g 
    
    for i in range (0,len(data2) - 1,2):
        g.insert_edge(data2[i],data2[i+1]) # call insert_edge to create edge
    

# DFS graph method ... generic type for adjacency list graph
def dfs(v):
    if v.getDest() not in visited:
        connected[connected_component].append(v.getDest().getId()) # adding the vertex to component
        visited.append(v.getDest())
        dfs(v.getDest().firstEdge())

    v = v.getNext()
    if v != None:
        dfs(v)


def isCyclic(graph):
    myList = []
    for i in visited:
        for j in graph.get_vertices().values().firstEdge():
            if i == j.getDest():
                myList.append(j.getSource())
    print(myList)


visited = []
connected = {}      
connected_component = 0
# keeping track of connected components by implementing DFS
for u in g.get_vertices().values():
    if u not in visited:
        connected_component += 1 # component number
        connected[connected_component] = [u.getId()] # component list
        visited.append(u) 
        dfs(u.firstEdge())


print("Read", g.vertexNum, "cities", int(g.edgeNum/2), "edges")   
# print()
print("Number of connected components:", connected_component)  
# print()
for key, value in connected.items():
    print("Connected Component",key,":")
    for j in value:
        print(j)
    print()

# print(g.myFunc())
for u in visited:
    print(u.getId())
# print(isCyclic(g))