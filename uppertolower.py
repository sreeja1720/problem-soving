n=input()
result=""
for i in n:
    if(97<=ord(i)<=123):#a->A  if('a'<=i<='z')
        result+=chr(ord(i)-32)
    else:
        result+=chr(ord(i)+32)
print(result)



#another way
if('a'<=i<='z')
