d = {}
s=''
while s!='stop':
    b=dict([input().split()])
    print(b.get('stop') )
    if b.get('stop'):
        s='stop'
    else:
        d.pop(b)
    
print (d)
