def twosum(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high):
        Sum=nums[low]+nums[high]
        if(Sum==target):
            return "yes"
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
    return "No"
nums=list(map(int,input().split()))
target=int(input())
print(twosum(nums,target))