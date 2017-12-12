from edge import Edge

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
		e = Edge(origin, destination, element)
		self._adjacent.append(e)