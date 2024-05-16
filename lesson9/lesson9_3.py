class MyExceptionFact(Exception):
    pass

def fact(n):
    if 0 <= n <= 1:
        return 1
    if n<0:
        raise MyExceptionFact("n<0")
    return fact(n - 1) * n

n=5
try:
    print(f"{n}! = {fact(n)}")
except (MyExceptionFact) as e:
    print(f"{e} {n}! does not exist")
