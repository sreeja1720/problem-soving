a=8
rem=""
while a:
    rem+=str(a&1)
    a=a>>1
print(rem[::-1])
