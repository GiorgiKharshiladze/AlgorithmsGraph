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