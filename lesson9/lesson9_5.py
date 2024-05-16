some_list1 = [1, 2, 3, [4, [5, 6], 7], 8, 9]
some_list2=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]


level=-1
def PrintList(MyList, Char="-"):
    global level
    level+=1
    for item in MyList:
        if isinstance(item, list):
            PrintList(item)
        else:
            print((Char*level),item) 
    level-=1

PrintList(some_list2)
