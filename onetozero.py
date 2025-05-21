def bit(a,i):
    mask=1<<i
    mask=~mask
    return a&mask
print(bit(5,0))