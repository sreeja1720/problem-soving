def power(x,n):
    if n<0:
        x=1/x
    n=abs(n)
    ans=1
    for i in range(n):
        ans=ans*x
    return ans
n=int(input())
x=int(input())
print(power(x,n))