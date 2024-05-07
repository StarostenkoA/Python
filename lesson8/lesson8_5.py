def count_char(str):
    d=dict()
    for c in str:
        if d.get(c):
            d[c]+=1
        else:
            d[c]=1
    print(d)

count_char("aabcccdddddd") 
