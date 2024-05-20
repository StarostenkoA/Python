def ex_decorator(func):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except BaseException as e:
            print(f"in finction {func.__name__} error - {str(e)}")
        
    return wrapper

@ex_decorator
def exept():
    error=7/0
    
exept()
