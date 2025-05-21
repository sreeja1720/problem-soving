from math import *
def banana(arr,k):
    low=1
    high=max(arr)
        
    while(low<=high):
        div=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/div)
        
            if(time<=k):
                
                high=div-1
            
            else:
                low=div+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(banana(arr,k))