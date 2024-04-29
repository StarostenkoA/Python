d = {'one':11, 'two':22, 'hello':'python', True:False}
num=input("enter num for del:")
d.pop(list(d)[int(num)])
print(d)
