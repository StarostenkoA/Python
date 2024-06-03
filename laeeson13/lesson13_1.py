import re
import datetime
import random

class User():
    __password = ''
     
    def __init__(self, name, login, password="") -> None:
        if not password:
            password=self.genpass()
            print(f"New generated password - {password}")
        self.name = name
        self.login = login
        self.password = password
        self.subscription_mode='free'
        self.subscription_date=datetime.date.today()+datetime.timedelta(days=30)
        self.is_blocked=False
    
    def bloc(self, blocked):
        self.is_blocked=blocked

    def check_subscr(self, datesub=0):
        subb=False
        if not datesub:
            datesub=datetime.date.today()
        else:
            datesub= datetime.datetime.strptime(datesub, "%Y-%m-%d").date()
        subb= self.subscription_date> datesub
        return (subb, self.subscription_mode, (self.subscription_date - datesub).days)
            
    def genpass(self):
        chars1 = 'abcdefghijklnopqrstuvwxyz'
        chars2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars3 = '1234567890'
        passw =''
        for i in range(2):
            passw += random.choice(chars1)
            passw += random.choice(chars2)
            passw += random.choice(chars3)
        return passw

    def change_pass(self, passw=0):
        if not passw:
            passw=self.genpass()
            print(f"New generated password - {passw}")
        self.password=passw

    def get_info(self):
        print(f"User name-{self.name}")
        print(f"User login-{self.login}")
        print(f"User subscription_mode-{self.subscription_mode}")
        print(f"User subscription_date-{self.subscription_date}")
        if self.is_blocked:
            print(f"User blocked")

    @property #getter  
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val):
        res = re.search(r'[a-zA-Z0-9-_]{6,}$', val)
        if res:    
            self.__password=val
        else:
            raise ValueError("Password not valid")
      
            

#user = User('Vasia','vasia1999','dvejnvnju&&98')
user = User('Vasia','vasia1999')

user.get_info()
#print(user.check_subscr('2024-07-01'))
print(user.check_subscr('2024-08-01'))
