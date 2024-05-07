latin="abcdefghijkl"
text = input("Enter digits: ")
newstr=''
for a in text:
    newstr += latin[int(a)]
print(newstr)
