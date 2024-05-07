lst = [input() for i in range(3)]
print(lst)
for i in lst:
    a=1
    for k in i: 
        print(a*k, end = '')
        a=a+1
    print(' ', end = '')
