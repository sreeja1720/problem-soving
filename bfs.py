def breadthFirstSearch(i,visited,q,adj,ans):
    while(q):
        node=q.pop(0)
        for it in adj[node]:
            if (visited[it]==0):
                visited[it]=1
                q.append(it)
        ans.append(node)
def bfs(adj):
    ans=[]
    v=len(adj)
    visited=[0]*v
    for i in range(0,v):
        if(visited[i]==0):
            visited[i]=1
            q=[i]
            breadthFirstSearch(i,visited,q,adj,ans)
    return ans
adj=[[1,2],[0,3],[0,6,5],[1],[3],[2],[2]]
print(bfs(adj))
