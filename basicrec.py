def fun(n):
    if n<=1:
        return 1
    fun(n-1)
    return n+fun(n-2)
print(fun(5)) 

'''print(n)
    fun(n-1)
    print(n)
print(fun(5))'''