a1=356
a2=4
a3=45
a4=78.34

if isinstance(a1, float) and isinstance(a2, float) and isinstance(a3, float) and isinstance(a4, float):
    print("True, all float")

if isinstance(a1, str) or isinstance(a2, str) or isinstance(a3, str) or isinstance(a4, str):
    print("True, >1 string")
    
if isinstance(a1, int) and isinstance(a3, int) or isinstance(a2, int) and isinstance(a4, int) or isinstance(a3, int) and isinstance(a4, int):
    print("True, para int")
