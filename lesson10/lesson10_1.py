def dict_from_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
    if not all(map(lambda i: isinstance(i, int), args)):
        raise ValueError("All pos args must by int")
    
    if not all(map(lambda i: isinstance(i, str), kwargs.values())):
        raise ValueError("All args keys must by str")

    SumArgs=sum(args)
    MaxVal = len(kwargs[max(kwargs)])

    DictForReturn={}
    DictForReturn["args_sum"]=SumArgs
    DictForReturn["kwargs_max_len"]=MaxVal
    return DictForReturn

print (dict_from_args(1,2,3,4,5,6,first="qwerty",second="qazwsxedc"))
