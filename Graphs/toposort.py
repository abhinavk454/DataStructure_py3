from undirectedgraph import vertex,undir

def toposort_h(w,ctime,sortv):
    w.intime=ctime
    w.status="inprocess"
    ctime+=1
    for v in w.getneighbour():
        if v.status=="unvisited":
            ctime=toposort_h(v,ctime,sortv)
            ctime+=1
    w.outtime=ctime
    w.status="done"
    sortv.insert(0,w)
    return ctime

def toposort(graph):
    startv=graph.vertex[0]
    sortv=[]
    for v in graph.vertex:
        v.status="unvisited"
        v.intime=None
        v.outtime=None
    toposort_h(startv,0,sortv)
    #print(sortv)
    return sortv

v1=vertex(5)
v2=vertex(8)
v3=vertex(7)
v4=vertex(9)

g=undir()

g.addvertex(v1)
g.addvertex(v2)
g.addvertex(v3)
g.addvertex(v4)

g.addedge(v1,v2)
g.addedge(v2,v3)
g.addedge(v3,v4)
g.addedge(v4,v1)

t=toposort(g)
for v in t:
    print(v)