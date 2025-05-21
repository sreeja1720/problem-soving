def bit(a,i):
    mask=1<<i 
    return a| mask
print(bit(8,2))