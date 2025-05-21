s1=input()
s2=input()
result=""
i=0
while(i<len(s1) and i<len(s2)):
    result+=(s1[i]+s2[i])
    i+=1
while(i<len(s1)):
      result+=chr(ord(s1[i])-32)
      i+=1
while(i<len(s2)):
    result+=chr(ord(s2[i])-32)
    i+=1
print(result)
