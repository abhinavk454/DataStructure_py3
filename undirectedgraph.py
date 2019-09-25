class vertex:
	def __init__(self,value):
		self.value=value
		self.neighbour=[]
		self.intime=None
		self.outtime=None
		self.status="unvisited"
	def addneighbour(self,data):
		self.neighbour.append(data)
	def find(self,value):
		if value in self.neighbour:
			return True
		return False
	def getneighbour(self):
		return self.neighbour
	def __str__(self):
		return str(self.value)

class undir:
    def __init__(self):
        self.vertex=[]
    def addvertex(self,v):
        self.vertex.append(v)
    def addedge(self,vertex1,vertex2):
        vertex1.addneighbour(vertex2)
        #vertex2.addneighbour(vertex1)
    def findedge(self):
        ret=[]
        for v in self.vertex:
            ret+=[[u,v] for u in v.neighbour]
        return ret
    def __str__(self):
        r1="vertex :"
        for v in self.vertex:
            r1+=str(v)+","
        r1+="\nEdge :\n"
        for a,b in self.findedge():
            r1+="("+str(a)+","+str(b)+")"
        return r1
    
#v1=vertex(5)
#v2=vertex(6)
#v3=vertex(7)
#v4=vertex(8)
#
#g=undir()
#
#g.addvertex(v1)
#g.addvertex(v2)
#g.addvertex(v3)
#g.addvertex(v4)
#
#g.addedge(v1,v2)
#g.addedge(v2,v3)
#g.addedge(v3,v4)
#g.addedge(v4,v1)
#
#print(g)