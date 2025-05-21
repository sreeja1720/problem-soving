def func(a,i):
    mask=1<<i
    return 1 if mask&a>0 else 0
print(func(5,2))