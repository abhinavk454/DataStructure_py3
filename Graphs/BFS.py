import math

inf=math.inf

class vertex:
    def __init__(self,value):
        self.value=value
        self.inNeighbour=[]
        self.outNeighbour=[]
        self.color="white"
        self.pi=None#predecessor
        self.dist=inf
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

def enqueue(Q,v):
    Q.insert(0,v)
    
def dequeue(Q):
    return Q.pop()

def BFS(G,s):
    Q=[]
    for u in G.vertex:
        u.color="white"
        u.pi=None
        u.dist=inf
    s.color="gray"
    s.dist=0
    s.pi=None
    enqueue(Q,s)
    while(Q!=[]):
        u=dequeue(Q)
        for v in u.outNeighbour:
            if v.color=="white":
                v.color="gray"
                v.dist=u.dist+1
                v.pi=u
                enqueue(Q,v)
        u.color="black"
    return G

r1=vertex(1)
r2=vertex(2)
r3=vertex(3)
r4=vertex(4)
#v=vertex('v')
#w=vertex('w')
#x=vertex('x')
#y=vertex('y')

G=graph()

for i in [r1,r2,r3,r4]:
    G.addVert(i)

for u,v in [[r3,r2],[r1,r2],[r2,r3],[r4,r4],[r1,r2],[r2,r3],[r3,r4],[r4,r2]]:
    G.addBie(u,v)
    
G=BFS(G,r2)
#for i in range(len(G.vertex)):
#    print(G.vertex[i].value ,G.vertex[i].dist)
def printpath(G,r2,v):
    if r2==v:
        return
    elif v.pi==None:
        print("No path exists :")
        return
    else:
        printpath(G,r2,v.pi)
        print(v.dist +1)

printpath(G,r2,r4)