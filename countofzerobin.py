
 # count of zeroes
a=8
count=0
while a:
    if a&1!=1:
        count+=1
    a=a>>1
print(count)
 # count of zeroes