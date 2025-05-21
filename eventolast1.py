l=list(map(int,input().split()))
n=len(l)
k=0
for i in range(n):
    if l[i]%2!=0:
        temp=l.pop(i)
        l.insert(k,temp)
        k+=1
print(l)
