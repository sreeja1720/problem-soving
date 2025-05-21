n=len(nums) #tc=O(N)
d={}        #sc=O(N)
for a in range(0,n):
    b=target-nums[a]
    if(b in d):
        return [a,d[b]]
    else:
        d[nums[a]]=a