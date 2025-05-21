def nthroot(n,m):
    ans=-1
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        elif(mid**n<m):
            low-mid+1
    return ans
n=int(input())
m=int(input())
print(nthroot(n,m))
            





# basic program using linear search

""""def sqrt(n,m):
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n,m=int(input())
print(sqrt(n,m))"""""