string=input("enter a, b, c, d:")
sum=0
for char in string:
    if char == "a":
        sum+=10
    elif char == "b":
        sum+=20
    elif char == "c":
        sum+=30
    elif char == "d":
        sum+=40
    else:
        print(f"{char} - Unknown char")
print(f"All score={sum}")
