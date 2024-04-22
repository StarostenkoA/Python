# 1. 
a1 = input('Enter value1: ')
a2 = input('Enter value2: ')
a3 = input('Enter value3: ')
print(a1, a2, a3)
print(a1, a2, a3, sep=":")
print('-', a1, '\n-', a2, '\n-', a3)


#2
b1=input('Enter int value1: ')
b2=input('Enter int value2: ')
print(int(b1)**int(b2))

#3
c=input('Enter phone purchase price: ')
print('Selling price - ', int(c)*1.3)
print('sale price with 5% discount - ', int(c)-int(c)*0.05)
print('sale price with 10% discount - ', int(c)-int(c)*0.1)
print('sale price with 15% discount - ', int(c)-int(c)*0.15)

#4
d1=input('Enter int value1: ')
print('thousands - ', int(int(d1)/1000))
print('soten - ', int(int(d1)%1000)//100)
print('dec - ', int(int(d1)%100)//10)
print('ed - ', int(int(d1)%10))
