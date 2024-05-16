MyList=['string',12,True]

print(type(MyList[1]))

print(list(filter(lambda x:True if isinstance(x, str) else False, MyList)))
print(list(filter(lambda x:True if isinstance(x, bool) else False, MyList)))
