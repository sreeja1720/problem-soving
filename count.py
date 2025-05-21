def count(a):
    if a%10==0: #if a==0  return 0 another
        return 1
    return 1+count(a//10)
print(count(1234))