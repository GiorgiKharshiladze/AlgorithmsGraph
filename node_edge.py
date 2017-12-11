class edge:
    def __init__(self, source, destination, nexts = None):
        self._source = source
        self._destination = destination
        self._next = nexts
    
    def getDest(self):
        return self._destination

    def getSource(self):
        return self._source
    
    def getNext(self):
        return self._next 


class node:
    
    counter = 0
    
    def __init__(self,key):
        self._id = key
        self._head = None
        self._index = node.counter
        node.counter += 1
        
    def getId(self):
        return self._id
    
    def modNode(self, new_key):
        self._id = new_key
        
    def addFirst(self, source, destination):
        self._head = edge(source, destination)
        self.position = self._head
    
    def addEdge(self, source, destination):
        self.element = edge(source, destination)
        self.position._next = self.element
        self.position = self.element
    
    def firstEdge(self):
        return self._head
    
    def getIndex(self):
        return self._index