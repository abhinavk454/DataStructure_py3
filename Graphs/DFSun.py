from undirectedgraph import vertex,undir
def DFS_helper(w,ctime):
    w.intime=ctime
    ctime+=1
    w.status="inprocess"
    #print(w)
    for vert in w.getneighbour():
        if vert.status=="unvisited":
            ctime=DFS_helper(vert,ctime)
            ctime+=1#makes vert.status done and returns to previous
    w.outtime=ctime
    w.status="done"
    return ctime

def DFS(w,graph):
    for vert in graph.vertex:
    	vert.status="unvisited"
    	vert.intime=None
    	vert.outtime=None
    return DFS_helper(w,0)

v1=vertex(5)
v2=vertex(6)
v3=vertex(7)
v4=vertex(8)

g=undir()

g.addvertex(v1)
g.addvertex(v2)
g.addvertex(v3)
g.addvertex(v4)

g.addedge(v1,v2)
g.addedge(v2,v3)
g.addedge(v3,v4)
g.addedge(v4,v1)

print(DFS(v1,g))