str="31a4b111c"
res="";num=""
for i in str:
    if i.isdigit():
        num+=i
        else:
            res+=int(num)* i
print(res)
