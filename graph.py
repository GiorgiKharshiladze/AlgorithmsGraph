from node_edge import node, edge

class graph:
    
    def __init__(self):
        self._vertices = {}
        self.vertexNum = 0
        self.edgeNum = 0
    
    # Method of insert node in the graph
    def insert_node(self, key):
        self.vertexNum += 1
        self._vertices[key] = node(key)
        return self._vertices[key]
    
    # Return this list of nodes in the graph 
    # self.vertice = {(Name: Node)}
    def get_vertices(self):
        return self._vertices
    
    # Method of search city and return the index of the node
    def searchCity(self, city):
        if city in self._vertices:
            return self._vertices[city].getIndex()
        else:
            return self.insert_node(city).getIndex()
    
    # Method to insert edge
    # Source and destination can be string representing name of the source and destination
    # Source and destination can be object of source and destination
    # sourcename and destination name not the objects
    
    def insert_edge(self, source, destination):
        self.edgeNum += 1
        if source in self._vertices:
            source = self._vertices[source]
        else:
            source = self.insert_node(source)
            
        if destination in self._vertices:
            destination = self._vertices[destination]
        else:
            destination = self.insert_node(destination)
        
        if source._head == None:
            source.addFirst(source, destination)
        else:
            source.addEdge(source, destination)
       
    # support method for cyclic
    def cyclic_test(self, v, parent):
        if v.getDest() not in self.visited:
            self.visited.append(v.getDest())
            return self.cyclic_test(v.getDest().firstEdge(),v)
                
        next_edge = v.getNext()
        if next_edge != None:
            if parent != next_edge.getDest():
                return True
            return self.cyclic_test(next_edge, v)
        return False


    # method to find cycle in graph, return true if cyclic
    def cyclic(self):
        self.visited = []
        for u in self._vertices.values():
            if u not in self.visited:
                self.visited.append(u)
                v = u.firstEdge()
                cycle = self.cyclic_test(v, u)
        return cycle


        
    def myFunc(self):

        print("source, destination")
        for u in self._vertices.values():
            print(u.getId())
            print(u.getIndex())
            print(u.firstEdge().getSource().getId(),"-",u.firstEdge().getDest().getId())