def towerofhanoi(n,src,tar,aux):
    if n == 1:
        return 1
    x1=(n-1,src,aux,tar)
    x2=(n-1,aux,tar,src)
    return x1 + 1 + x2
n=int(input())
src=input()
tar=input()
aux=input()
print(towerofhanoi(n,src,tar,aux))
