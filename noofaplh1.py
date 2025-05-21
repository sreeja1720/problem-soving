str="10a4b11c"
res="";num=""
for i in str:
    if i.isdigit():
        num+=i
    else:
        res+=int(num)* i
        num=""
print(res)
