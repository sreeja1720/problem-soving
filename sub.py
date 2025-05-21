s=input()
sub=input()
if(sub in s):
    print(True)
if(len(s)>len(sub)):
    s=s+s
    if(sub in s):
        print(True)
    else:
        print(False)
