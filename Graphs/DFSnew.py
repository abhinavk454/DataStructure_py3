import math
inf=math.inf
class vertex: 
    def __init__(self,value):
        self.value=value
        self.inNeighbour=[]
        self.outNeighbour=[]
        self.d=inf#discovery time
        self.f=inf#finish time
        self.color="White"
        self.pi=None
    def addIn(self,value):
        self.inNeighbour.append(value)
    def addOut(self,value):
        self.outNeighbour.append(value)
    def getIn(self):
        return self.inNeighbour
    def getOut(self):
        return self.outNeighbour
    def findIn(self,value):
        if value in self.inNeighbour:
            return True
        return False
    def findOut(self,value):
        if value in self.outNeighbour:
            return True
        return False
    def find(self,value):
        if value in self.inNeighbour or value in self.outNeighbour:
            return True
        return False
    def __str__(self):
        return str(self.value)

class graph:
    def __init__(self):
        self.vertex=[]
    def addVert(self,vert):
        self.vertex.append(vert)
    def addDie(self,u,v):
        u.addOut(v)
        v.addIn(u)
    def addBie(self,u,v):
        self.addDie(u,v)
        self.addDie(v,u)
    def getEdge(self):
        ret=[]
        for v in self.vertex:
            ret+=[[v,u] for u in v.getOut()]
        return ret
    def __str__(self):
        ret="vertex :"
        for v in self.vertex:
            ret+=str(v)+" "
        ret+="edges :"
        for a,b in self.getEdge():
            ret+="("+str(a)+","+str(b)+")"
        return ret

def DFS_visit(G,time,u):
    time=time+1
    u.d=time
    u.color="gray"
    for v in u.outNeighbour:
        if v.color=="white":
            v.pi=u
            time=DFS_visit(G,time,v)
    u.color="black"
    time=time+1
    u.f=time
    return time
def DFS(G):
    for v in G.vertex:
        v.color="white"
        v.pi=None
    time=0
    for u in G.vertex:
        if u.color=="white":
            time=DFS_visit(G,time,u)
    return G

r=vertex('r')
s=vertex('s')
t=vertex('t')
u=vertex('u')
v=vertex('v')
w=vertex('w')
x=vertex('x')
y=vertex('y')

G=graph()

for i in [r,s,t,u,v,w,x,y]:
    G.addVert(i)

for u,v in [[r,s],[s,t],[t,u],[u,v],[v,w],[w,x],[x,y]]:
    G.addBie(u,v)
    
G=DFS(G)

for i in range(len(G.vertex)):
    print(G.vertex[i].d,G.vertex[i].f,G.vertex[i].pi)#d is discovery time f is final time