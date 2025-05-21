def selectionsort(arr):
    for i in range(0,n):
        Min=i
        for j in range(i+1,n):
            if(arr[j]<arr[Min]):
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(selectionsort(arr))
## we push smallest elements to first by finding min from array and then swap 