class Graph:
    def __init__(self):
        self.V = set()
        self.E = []
    
    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, vertex):
        if vertex in self.V:
            self.V.remove(vertex)
            self.E = [(u, v, w) for (u, v, w) in self.E if u!= vertex and v!=vertex]

    def add_edge(self, u, v, w):
        if u in self.V and v in self.V:
            self.e.append((u,v,w))
    
    def remove_edge(self, u, v):
        self.E = [(x,y,z) for x,y,z in self.E if (u,v) != (u,v) and (x,y) != (v,u)]

