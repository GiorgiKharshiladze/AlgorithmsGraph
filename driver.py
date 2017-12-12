from node import Node
from edge import Edge
from graph import Graph
from stack import Stack


def dfs (v, visited):
	if len(visited) == 0:
		visited.append(v.source())
	if v.destination() not in visited:
		visited.append(v.destination())
		dfs(v.destination().firstEdge(), visited)
	if v!= None:
		for i in (v.destination().adjacent()):
			if i.destination() not in visited:
				dfs(i, visited)
	return visited


def graphBuilder():
	filename = input("Enter the name of your file (Must be present in current directory): ")
	file = open(filename)
	myGraph = Graph()
	edge_list = []
	node_list = []
	for line in file:
		for i in line.split():
			new = [i.split('-')]
			edge_list.extend(new)
	file.close()
	for element in edge_list:
		if element[0] not in node_list:
			node_list.append(element[0])
		if element[1] not in node_list:
			node_list.append(element[1])
	for i in range(len(node_list)):
		myGraph.insertNode(node_list[i], i)

	for element in edge_list:
		origin = element[0]
		destination = element[1]
		origin_index = myGraph.searchCity(origin)
		destination_index = myGraph.searchCity(destination)
		myGraph.nodeList[origin_index].addEdge(myGraph.nodeList[origin_index], myGraph.nodeList[destination_index])
	return myGraph

def cyclicDFS(graph, start):
	vertexList, edgeList = graph
	visitedVertex = []
	stack = [start]
	adjacencyList = [[] for vertex in vertexList]
	
	for edge in edgeList:
		adjacencyList[edge[0]].append(edge[1])
		
	while stack:
		current = stack.pop()
		for neighbor in adjacencyList[current]:
			if not neighbor in visitedVertex:
				stack.append(neighbor)
		visitedVertex.append(current)
	return visitedVertex

def checkCyclic(graph):

	for i in graph.getNodes():
		vertexList.append(i.index())
		for j in i.adjacent():
			edgeList.append((j.source().index(), j.destination().index()))

	all_visited = cyclicDFS(graphs, 0)

	return isRepeated(all_visited)

def isRepeated(c):
	myset = set()
	for i in c:
		lst = len(myset)
		myset.add(i)
		if len(myset) == lst:
			return "Graph contains a cycle"
	return "Graph does not contain a cycle"


def showComps(graph, c_c):
	nameList = graph.nodeList
	while len(nameList) != 0:
		visited = dfs(nameList[0].firstEdge(), [])
		c_c += 1
		connected[c_c] = visited
		for i in visited:
			if i in nameList:
				nameList.remove(i)
	
	for key,value in connected.items():
		print (" Connected Component", key,":")
		for j in value:
			print ("    ",j.name())



if __name__ == "__main__":
	

	myGraph = graphBuilder()

	# Global variables for connected components
	visited = []
	connected = {}         
	connectedComp = 0
	cityList = []

	# Global variables for cyclic
	vertexList = []
	edgeList = []
	graphs = (vertexList, edgeList)

	# g.showGraph()

	cyclic = checkCyclic(myGraph)


	print("Read", myGraph.numCities() ,"cities and", myGraph.numEdges() ,"edges")

	showComps(myGraph, connectedComp)
	
	print(cyclic)
