users=[
    {'FIO':'Starostenko','d':'Capt','b':'19750113','n':['C#','Python','Asm','C++'],'children':[{'name':'Ilya','b':"20030516"},{'name':'Lena','b':"20120118"}]},
    {'FIO':'Konon','d':'Capt','b':'19810214','n':['Python'],'children':[{'name':'Don','b':"20180707"}]},
    {'FIO':'Mel','d':'Capt','b':'19890315','n':['Python','Pascal'],'children':[{'name':'Vas','b':"20190816"}]}
    ]
name = 'Starostenko'#input('Enter name:')
for person in users:
    if person['FIO'] == name:
        print(person)
