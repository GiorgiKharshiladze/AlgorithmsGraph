class Graph:

	def __init__(self):
		self.nodeList = []

	def insertNode(self, name, index):
	#Inserting a node by adding it to the primary node list. 
		node = Graph.Node(name, index)
		self.nodeList.append(node)
		return node 

	def searchCity(self, name):
	#Check if a city is already present in the node list, otherwise add it in.
		list_length = len(self.nodeList) 
		for i in range (list_length):
			if self.nodeList[i].name() == name:
				return i 
		insertNode(name, list_length)
		return (list_length)

	
	def showGraph(self):
	#Test function to see if ADTs are functional (matching with given output files). 
		counter = 0
		for node in self.nodeList:
			print ("Node:", node.index(), " ",  "Name:", node.name()) 
			for edge in node.adjacent():
				counter +=1
				print ("Edge:", edge.otherend(node))
		print ("Cities: ", (len(self.nodeList)))
		print ("Edges: ", counter//2)


	class Edge: 
		# The initialization function for the Edge ADT. 
		def __init__(self, origin, destination, x):
			self._origin = origin 
			self._destination = destination 
			self._element = x 

		# The other-end function for the Edge ADT. 
		def otherend(self, destination): 
			return self._destination.index() 

		def destination(self):
			return self._destination

		def source(self):
			return self._origin

		# Returns a pointer to the next edge. 
		def pointer(self):
			return self._element

	class Node:
		#Initialization of the Node ADT. 
		def __init__(self, name, index=None):
			self._index = index 
			self._name = name 
			self._adjacent = [] 
			self._pointer = None

		#Selector Functions to return the value of each data field. 
		def index(self):
			return self._index 

		def name(self):
			return self._name 

		def adjacent(self):
			return self._adjacent[::-1]

		#First edge function that returns a pointer/refernece to the first edge in a list of adjacent nodes. 
		def firstEdge(self):
			return self._adjacent[0]

		#Inserting an edge. 
		def addEdge(self, origin, destination, element=None):
			e = Graph.Edge(origin, destination, element)
			self._adjacent.append(e)

# def dfs(node, visited):
# 	visited.append(node)
# 	adjacencyList = node.adjacent()
# 	next_node = visitedHelper(adjacencyList, visited, 0)
# 	print (next_node.name())
# 	dfs(next_node, visited)

# def visitedHelper(list1, list2, i):
# 	i = i 
# 	if i <= (len(list1)):
# 		if list1[i] in list2:
# 			print (i)
# 			i+=1
# 			visitedHelper(list1, list2, i)
# 		else:
# 			return list1[i].destination()

# def dfs(v, l1):
# 	if v.destination() not in visited:
# 		visited.append(v.destination())
# 		dfs(v.destination().firstEdge(), visited)
# 	v = v.pointer()
# 	if v != None:
# 		dfs(v, visited)

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

comps = {}
count = 0
dfsList = []	

def connected(graph, visList):
	
	newList = []

	# if len(visList) == len(graph.nodeList()):
	# 	return comps
	# else:	
	for node in graph.nodeList:
		if node not in visList:
			newList.append(node)

	if len(newList) == 0:
		return comps
	else:
		count+=1
		dfsList = dfs(newList[0].firstEdge(), [])
		connected(graph, dfsList)


	# dfs(newList[0].firstEdge(), visList)
	# if len(newList) != 0:
	# 	connected(graph, dfsList)
	# else:
	# 	dfsList = dfs(newList[0].firstEdge(), visList)
	# return comps	

# def dfsUtil(node):


# 	start = graph.index(0)
# 	stack = [start]
# 	while stack:
# 		node = stack.pop()
# 		if node not in visited:
# 			visited.add(node)
# 			stack.push



#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited

def testFunction1():
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

if __name__ == "__main__":
	g = testFunction1()
	g.showGraph()
	#print (dfs(g,0))
	adjacentList = g.nodeList[1].adjacent()
	print (connected(g,[]))

	# for i in myList:
	# 	print(i.name())

	# for i in adjacentList:
	# 	print (i.source().firstEdge(), i.destination().firstEdge())
	# for i in traversal:
	# 	print (i.source().name(), i.destination.name())

	# visited = []
	# connected = {}         
	# connected_component = 0
	# # keeping track of connected components by implementing DFS
	# for u in g.nodeList():
	# 	if u not in visited:
	# 		connected_component += 1 # component number
	# 		connected[connected_component] = [u.name()] # component list
	# 		visited.append(u)
	# 		dfs(u.firstEdge())
	# print (connected_component)


















