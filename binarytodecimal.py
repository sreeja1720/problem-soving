a=input()  
a=a[::-1]
res=0
for i in range(len(a)):
    res+=int(a[i])*(2**i)
print(res)
