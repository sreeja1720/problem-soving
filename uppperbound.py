def lowerbound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(lowerbound(arr,target))
