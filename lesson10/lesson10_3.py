def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Executing function {func.__name__} with arguments args-{args} kwargs- {kwargs}")
        func(*args,**kwargs)
        print(f"{func.__name__} - completed")
    return wrapper

@log_decorator
def hello(name):
    print(f"Hello, {name}")
    
hello("Vasia")
