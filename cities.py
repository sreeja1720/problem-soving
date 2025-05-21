def breadthFirstSearch(i,visited,q,adjList):
    while(q):
        node=q.pop(0)
        for it in adjlist[node]:
            if(visited[it]==0):
                visited[it]=1
                q.append(it)
            
def numProvinces(adj,v):
    adjList=[]
    for  i in range(v):
        adjList.append([])
    n=len(adj)
    m=len(adj[0])
    for i in range(n):
        for j in range(m):
            if(adj[i][j]==1 and i!=j):
                adjList[i].append(j)
                adjList[j].append(i)
    
visited=[0]*v
c=0
for i in range(0,v):
    if(visited[i]==0):
        q=[i]
        breadthFirstSearch(i,visited,q,adj,ans)
        c+=1
return c
