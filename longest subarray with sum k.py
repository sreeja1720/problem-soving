def longestSubarray(arr, k):  
        # code here
    n=len(arr)
    d={}
    Sum=0
    maxLen=0
    for i in range(0,n):
        Sum+=arr[i]
        if(Sum==k):
            maxLen=i+1
        rem=Sum-k
        if(rem in d):
            maxLen=max(maxLen,i-d[rem])
        if(Sum not in d):
            d[Sum]=i
    return maxLen
arr=list(map(int,input().split()))
k=int(input())
print(longestSubarray(arr,k))