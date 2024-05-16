users=[{"name":"some_name", "login":"some_%login", "password":"some_password" },
 {"name":"first_name", "login":"first_,login", "password":"first_password" },
 {"name":"second_name", "login":"second_login", "password":"second_password" },
 {"name":"test_name", "login":"test_login", "password":"test" },
]

def filter_valid(login):
    valid =False
    for char in login:
        if  char =='_':
            valid=True
        elif char.isalpha():
            valid=True
        elif char.isdigit():
            valid=True
        else:
            valid =False
            return not valid
    return not valid

l1=list(filter(lambda x:True if len(x["password"])<5 else False, users))
print(l1)

ListNotValid=list(filter(lambda x:filter_valid(x["login"]), users))
for item in ListNotValid:
    print(f"Dear {item['name']}, your {item['login']} is not correct.")
