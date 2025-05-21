def insertionsort(arr):
    for i in range(0,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(insertionsort(arr))