l=list(map(int,input().split()))
n=len(l)
i=0
while i<n:
    if l[i]%2==0:
        l.append(l[i])
        l.pop(i)
        n-=1
    else:
        i+=1
print(l)

