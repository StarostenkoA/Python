a = []
b='1'
while b!='0':
    b=input("Enter:")
    if b!='0':
        a.append(int(b))
print(f"Average={sum(a)/len(a)}")
