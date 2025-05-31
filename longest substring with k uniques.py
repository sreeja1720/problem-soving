##optimal code##

"""def longestKSubstr(self, string, k):
    n=len(string)
    if(n==1):
        return 1
    dup=sorted(string)
    if(dup[0]==dup[n-1]):
        return -1
    if(len(set(dup))<k):
        return -1
    maxLen=0
    left=0
    right=0
    d={}
    while(right<n):
        if(string[right] in d):
            d[string[right]]+=1
        else:
            d[string[right]]=1
        if(len(d)>k):
            while(len(d)>k):
                d[string[left]]-=1
                if(d[string[left]]==0):
                    del d[string[left]]
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen"""

        












##brutee froce
def longest(s,k):
    n=len(s)
    maxLen=0
    if(n==1):
        return 1
    if(len(list(set(s)))==1): #we 1st convert it to set and we can find length of set so we convert it into list to get the length
        return -1
    if(len(set(s))<k):
        return -1
    for i in range(0,n):
        Set=set()
        for j in range(i,n):
            Set.add(s[j])
            if(len(Set)>k):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
s=input()
k=int(input())
print(longest(s,k))