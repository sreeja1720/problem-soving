str="31abc"
res="";num="";alp=""
i=0
while i<len(str):
    while str[i].isdigit():
        num+=str[i]
        i+=1
    while i<len(str) and str[i].isalpha():
        alp+=str[i]
        i+=1
    res+=int(num)*alp
    num=alp=""
print(res)
