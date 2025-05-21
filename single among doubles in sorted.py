##even,odd->left half and single is in right side
##odd,even->right half and single is in left side
def findOnce(nums):
    n=len(nums)
    if(n==1):
        return nums[0]
    elif(nums[0]!=nums[1]):
        return nums[0]
    elif(nums[n-1]!=nums[n-2]):
        return nums[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
            return nums[mid]
        elif((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):# u r in left half
            low=mid+1
        elif((mid%2==1 and nums[mid]==nums[mid+1]) or (mid%2==0 and nums[mid]==nums[mid-1])):#ur in right half
            high=mid-1
nums=list(map(int,input().split()))
print(findOnce(nums))