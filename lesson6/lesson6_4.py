string=input("Enter num:")
num=int(string)
count=0
if(num<20):
    for n in range(1, num+1):
        if (n%7 == 0):
            count+=1
if(num>20):
    for n in range(1, num+1):
        if (n%11 == 0):
            count+=1
print(count)
