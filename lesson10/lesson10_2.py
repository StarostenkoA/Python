def bread(func):
    def wrapper():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapper

def tomato(func):
    def wrapper():
        print("***  tomato  ****")
        func()
    return wrapper

def salad(func):
    def wrapper():
        print("~~~~ salad ~~~~~")
        func()
    return wrapper

def cheese(func):
    def wrapper():
        print("^^^^^cheese^^^^^")
        func()
    return wrapper

def onion(func):
    def wrapper():
        print("-----onion------")
        func()
    return wrapper

@bread
@onion
@tomato
def beef():
    print("###   beef   ###")

@bread
@cheese
@salad    
def chicken():
    print("|||| chicken||||")
   

chicken()
