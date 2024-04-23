#1
str1=input('enter string: ')
print("count str: ", len(str1))
print("count words: ", len(str1.split()))
b = str1.maketrans({"a":"","e":"","i":"","o":"","u":"","y":""})
b = str1.translate(b)
print("count glassn: ", len(str1)-len(b))

#2
a, b, c = input("enter 3 digits: ").split()
listD=[]
listD.append(int(a))
listD.append(int(b))
listD.append(int(c))
print(sum(listD))

#3
str3 = input("enter word: ")
print(str3[::-1])

#4
s = "name: Dmitro, fam: Ivanov, age: 18"
a1,b1,c1,=s.split(',')
a1,name=a1.split(':')
b1,fam=b1.split(':')
c1,age=c1.split(':')
print(name.strip(),fam.strip(),age.strip(), sep='\n')

#5
str5= "User with name <name> login on site in 15:00"
str51=input("enter name: ")
str52=str5.replace('<name>',str51)
print(str52)

#6
str6="This is test <start>string for tech<end> opation string"
print(str6[str6.find('<start>')+7:str6.find('<end>')])
