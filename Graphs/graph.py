class vertex:#directed graphs
    def __init__(self,v):
        self.inNeighbour=[]
        self.outNeighbour=[]
        self.value=v
        self.inTime=None
        self.outTime=None
        self.status="unvisited"    
    def hasOutNeighbour(self,v):
        if v in self.outNeighbour:
            return True
        return False    
    def hasInNeighbour(self,v):
        if v in self.inNeighbour:
            return True
        return False    
    def hasNeighbour(self,v):
        if v in self.inNeighbour or v in self.outNeighbour:
            return True
        return False    
    def getInNeighbour(self):
        return self.inNeighbour    
    def getOutNeighbour(self):
        return self.outNeighbour    
    def addInNeighbour(self,v):
        self.inNeighbour.append(v)        
    def addOutNeighbour(self,v):
        self.outNeighbour.append(v)        
    def __str__(self):
        return str(self.value)
    
class graph:
    def __init__(self):
        self.vertex=[]
    def addVertics(self,n):
        self.vertex.append(n)
    def addDiEdge(self,u,v):#adds directed edges frou to v
        u.addOutNeighbour(v)
        v.addInNeighbour(u)
    def addbiedge(self,u,v):#add edge in both diection
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)
    def getDirEdge(self):
        dire=[]
        for v in self.vertex:
            dire+=[[v,u] for u in v.outNeighbour]
        return dire
    def __str__(self):
        ret="Vertices :\n"
        for v in self.vertex:
            ret+=str(v)+","
        ret+="\nEdge :\n"
        for a,b in self.getDirEdge():
            ret += "(" + str(a) + "," + str(b) + ") "
        return ret
"""
class vert:
    def __init__(self,value):
        self.value=value
        self.inNeigh=[]
        self.outNeigh=[]
        self.Intime=None
        self.Outtime=None
        self.status="unvisited"
    def addInNeigh(self,data):
        self.inNeigh.append(data)
    def addOutNeigh(self,data):
        self.outNeigh.append(data)
    def getInNeigh(self):
        return self.inNeigh
    def getOutNeigh(self):
        return self.outNeigh
    def findInNeigh(self,v):
        if v in self.inNeigh:
            return True
        return False
    def findOutNeigh(self,v):
        if v in self.outNeigh:
            return True
        return False
    def findNeigh(self,v):
        if v in self.outNeigh or v in self.inNeigh:
            return True
        return False
    def __str__(self):
        return str(self.value)

vn1=vert(2)
vn2=vert(3)
vn3=vert(4)
vn4=vert(5)
vn5=vert(6)
vn6=vert(7)

vn1.addInNeigh(5)
vn1.addOutNeigh(7)
vn1.addInNeigh(1235)
vn1.getInNeigh()
vn1.findNeigh(5)
        
class graph:
    def __init__(self):
        self.vert=[]
    def addVert(self,n):
        self.vert.append(n)
    def addDiEdge(self,u,v):
        u.addOutNeigh(v)
        v.addInNeigh(u)
    def addBiEdge(self,u,v):
        self.addDiEdge(u,v)
        self.addDiEdge(v,u)
    def getDirEdge(self):
        dirc=[]
        for v in self.vert:
            dirc+=[[u,v] for u in v.outNeigh]
        return dirc
    def __str__(self):
        ret="vertice :\n"
        for v in self.vert:
            ret+=str(v)+","
        ret+="\nEdge :\n"
        for a,b in self.getDirEdge():
            ret+="("+str(a) +","+ str(b)+")"
        return ret

g=graph()
g.addVert(vn1)
g.addVert(vn2)
g.addVert(vn3)
g.addVert(vn4)
g.addVert(vn5)
g.addVert(vn6)

g.addBiEdge(vn1,vn2)
g.addBiEdge(vn2,vn6)
g.addBiEdge(vn1,vn5)
g.addBiEdge(vn6,vn5)
g.addBiEdge(vn4,vn5)
g.addBiEdge(vn3,vn4)
"""