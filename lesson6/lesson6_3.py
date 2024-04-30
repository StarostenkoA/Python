a,b,c,=input("enter 3 digit:").split()
if (int(a)>=int(b)):
    if(int(a)>=int(c)):
        print(a)
    else:
        print(c)
else:
    if(int(b)>=int(c)):
        print(b)
    else:
        print(c)
