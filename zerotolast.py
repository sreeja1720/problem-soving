l=list(map(int,input().split()))
n=len(l)
for i in range(n):
    if l[i]==0:
        l.append(0)
        l.pop(i)
print(l)
