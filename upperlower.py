n=input()
result=""
s="aeiou"
for i in n:
    if(i in s):
        result+=(chr(ord(i)-32))
    else:
        result+=i
print(result)
        
