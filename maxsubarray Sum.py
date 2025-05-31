####optimal##
def maxSum(nums):
    n=len(nums)
    maxSum=float("-inf")
    curr_sum=0
    for i in nums:
        curr_sum+=i
        maxSum=max(curr_sum,maxSum)
        if(curr_sum<0):
            curr_sum=0
    return maxSum
nums=list(map(int,input().split()))
print(maxSum(nums))

##brute force##
"""def maxSubarray(nums):
    n=len(nums)
    maxSum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxSum=max(maxSum,Sum)
    return maxSum
nums=list(map(int,input().split()))
print(maxSubarray(nums))
#nums:-2 -1 3 4 6 -1 -6 10 20
#output:36"""