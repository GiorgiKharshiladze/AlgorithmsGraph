from node import Node

class Graph:

	def __init__(self):
		self.nodeList = []

	def getNodes(self):
		return self.nodeList

	def insertNode(self, name, index): #Inserting a node by adding it to the primary node list. 
		node = Node(name, index)
		self.nodeList.append(node)
		return node

	def searchCity(self, name):
	#Check if a city is already present in the node list, otherwise add it in.
		list_length = len(self.nodeList) 
		for i in range (list_length):
			if self.nodeList[i].name() == name:
				return i 
		self.insertNode(name, list_length)
		return (list_length)

	def numCities(self):
		return len(self.nodeList)

	def numEdges(self):
		edges = 0
		for node in self.nodeList:
			for edge in node.adjacent():
				edges += 1
		edges //= 2
		
		return edges

	
	def showGraph(self):
	#Test function to see if ADTs are functional (matching with given output files). 
		for node in self.nodeList:
			print ("Node:", node.index(), " ",  "Name:", node.name()) 
			for edge in node.adjacent():
				print ("Edge:", edge.otherend(node))
		print ("Cities: ", self.numEdges())
		print ("Edges: ", self.numCities())