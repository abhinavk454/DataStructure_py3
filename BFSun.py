from undirectedgraph import vertex,undir

def BFS(w,graph):
    for v in graph.vertex:
        v.status="unvisited"
    n=len(graph.vertex)
    ls=[[] for i in range(n)]
    ls[0]=[w]
    w.status="visited"
    for i in range(n):
        for u in ls[i]:
            for v in u.getneighbour():
                if v.status=="unvisited":
                    v.status="visited"
                    ls[i+1].append(v)
    return ls
G =undir()
for i in range(7):
    G.addvertex( vertex( i ) ) 
V = G.vertex
for pairs in [ (0,2), (0,4), (0, 6), (1, 3), (1, 4), (2, 3), (2, 6), (4, 5), (5,6) ]:
    G.addedge( V[pairs[0]], V[pairs[1]] )
print(G)

levels = BFS(G.vertex[1], G)
for i in range(len(levels)):
    print("Level", i, ":")
    for j in levels[i]:
        print("\t", j)
    
# now what's the distance from node 1 to node 6?
for i in range(len(levels)):
    if G.vertex[6] in levels[i]:
        print("distance from 1 to 6 is", i)
        break
#v1=vertex(5)
#v2=vertex(8)
#v3=vertex(7)
#v4=vertex(9)
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
#bfs=BFS(v1,g)