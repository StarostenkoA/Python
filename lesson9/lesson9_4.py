numbers  = [1,2,3,4,5,6,7,8,9]
list1=list(map(lambda x:x**2,numbers))
list2=list(map(lambda x: x if x % 2 else x+3,numbers))
list3=list(map(lambda x: x*3 if x % 2 else x*2,numbers))

print(numbers)
print(list1)
print(list2)
print(list3)
