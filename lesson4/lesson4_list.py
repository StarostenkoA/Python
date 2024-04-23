#1
from audioop import reverse
Mylist = [45,'string', 89, 637478]
print(Mylist[::-1])
for i in reversed(Mylist):
    print(i,end=' ')
print()

#2
a, b, c, d, e, = input("enter 5 names: ").split()
list2 = [ ]
list2.append(a)
list2.append(b)
list2.append(c)
list2.append(d)
list2.append(e)
print(sorted(list2))

#3
list3 = ['hello', 'python', 'interpetator', 'pep8', "123"]
list3[-1], list3[0] = list3[0], list3[-1]
print(list3)
print(list3.pop(2))

#4
list4 = ['hello', 'python', 'interpetator', 'pep8', "123"]
listCount = list(map(len, list4))
print(listCount)

#5
list5 = [1, 1, 2, 3, 21, 8, 13, 21, 34, 55, 89]
print(list5[::2])

#6
list6 = ['samsung', 'lg', 'xerox', 'bosch']
list6.remove('xerox')
print(list6)
