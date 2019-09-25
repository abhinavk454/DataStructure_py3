from graph import graph,vertex
def DFS_helper(w,currenttime,verbose=False):
    if verbose:
        print("Time",currenttime,"Entering :",w)
    w.inTime=currenttime
    currenttime+=1
    w.status="inprocess"
    for v in w.getOutNeighbour():
        if v.status=="unvisited":
            currenttime=DFS_helper(v,currenttime,verbose)
            currenttime+=1
    w.outTime=currenttime
    w.status="done"
    if verbose:
        print("Time",currenttime,"leaving :",w)
    return currenttime
def DFS(w,g,verbose=False):
    for v in g.vertex:
        v.status="unvisited"
        v.inTime=None
        v.outTime=None
    return DFS_helper(w,0,verbose)
    
vn1=vertex(2)
vn2=vertex(3)
vn3=vertex(4)
vn4=vertex(5)
vn5=vertex(6)
vn6=vertex(7)

g=graph()
g.addVertics(vn1)
g.addVertics(vn2)
g.addVertics(vn3)
g.addVertics(vn4)
g.addVertics(vn5)
g.addVertics(vn6)

g.addbiedge(vn1,vn2)
g.addbiedge(vn2,vn6)
g.addbiedge(vn1,vn5)
g.addbiedge(vn6,vn5)
g.addbiedge(vn4,vn5)
g.addbiedge(vn3,vn4)

DFS(vn1,g)