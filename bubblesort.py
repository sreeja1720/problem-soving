# we do adjacent swaps by finding the max element and fix last position every time
def bubblesort(arr):

    for i in range(n-1,-1,-1):
        for j in range(i):# j starts from 0
            if(arr[j]>arr[j+1]):# chesk first and next element
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(bubblesort(arr))
                
