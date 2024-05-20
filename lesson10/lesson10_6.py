def counter(n):
    i = n
    
    def func():
        nonlocal i
        i += 1
        return i
    
    return func


c1 = counter(1)
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3


c2 = counter(10)
print(c2())  # 1
print(c2())  # 2
print(c2())  # 3
