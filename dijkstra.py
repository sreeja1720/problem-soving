import heapq
def dijkstra(v,edge,src):
    adjList=[]
    for i in range(v):
        adjList.append([])
    for n,m,w in edge:
        adjList[n].append((m,w))
        adjList[m].append((n,w))
    distance=[float("inf")]*v
    pq=[]
    distance[src]=0
    heapq.heappush(pq,(0,src))
    while(pq):
        dist,node=heapq.heappop(pq)
        for adjNode,adjDist in adjList[node]:
            if(dist+adjDist<distance[adjNode]):
                distance[adjNode]=dist+adjDist
                heapq.heappush(pq,(dist+adjDist,adjNode))
    return distance
v=int(input())
src=int(input())
edge=[1,0,1],[1,2,3],[2,0,6],[2,1,3],[2,3,3],[3,0,2],[3,2,3]]s
print(dijkstra(v,edge,src))
