def fun(a):

    if a//10==0:
        return a
    
    return a%10+ fun(a//10)


print(fun(123))
'''' rev=a%10
sum=sum+rev*10
a//=10 '''