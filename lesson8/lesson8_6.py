def yes_or_no(list):
    
    for i in list:
        if(isinstance(i,int)!=True):
            return False

    f=dict()
    for i in list:
        if f.get(i):
            f[i]='no'
        else:
            f[i]='yes'
            
    print (f)
    return f.values()
        

print(yes_or_no([1,2,3,1,4]))
