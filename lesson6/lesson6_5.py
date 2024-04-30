year=[
    ['Jan','Winter',31],
    ['Feb','Winter',28],
    ['Mar','Spring',31],
    ['Apr','Spring',30],
    ['May','Spring',31],
    ['Jun','Summer',30],
    ['Jul','Summer',31],
    ['Aug','Summer',31],
    ['Sep','Autumn',30],
    ['Oct','Autumn',31],
    ['Nov','Autumn',30],
    ['Dec','Winter',31],
     ]
string=input("Enter num month:")
num=int(string)
if (num<1 or num >12):
    print("bad month")
else:
    print(year[num-1])    
