class vertex:
    def __init__(self,value):
        self.value=value;
        self.inNeighbour=[]
        self.outNeighbour=[]
        self.inTime=None
        self.ootTime=None
        self.status="unvisited"
    def addInNeighbour(self,var):
        self.inNeighbour.append(var)
    def addOutNeighbour(self,var):
        self.outNeighbour.append(var)
    def getInNeighbour(self):
        return self.inNeighbour
    def getOutNeighbour(self):
        return self.outNeighbour
    def findIn(self,val):
        if val in self.inNeighbour:
            return True
        return False
    def findOut(self,val):
        if val in self.outNeighbour:
            return True
        return False
    def find(self,val):
        if val in self.outNeighbour and val in self.inNeighbour:
            return True
        return False
    def __str__(self):
        return str(self.value)

class digraph:
    def __init__(self):
        self.vertex=[]
    def addVertex(self,v):
        self.vertex.append(v)
    def addDiedge(self,u,v):#u--->--v
        u.addOutNeighbour(v)
        v.addInNeighbour(u)
    def addBiedge(self,u,v):
        self.addDiedge(u,v)
        self.addDiedge(v,u)
    def reverseEdge(self,u,v):
        if u.findOut(v) and v.findIn(u):
            if v.findOut(u) and u.findIn(v):
                return
            self.addBiedge(v,u)
            u.outNeighbour.remove(v)
            v.inNeighbour.remove(u)
    def getDiredge(self):
        ret=[]
        for v in self.vertex:
            ret+=[[u,v] for u in v.outNeighbour]
        return ret
    def __str__(self):
        ret="Vertex :"
        for v in self.vertex:
            ret+=str(v)+" "
        ret+="Edge :"
        for a,b in self.getDiredge():
            ret+="("+str(a)+","+str(b)+")"
        return ret