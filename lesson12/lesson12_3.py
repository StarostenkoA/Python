from abc import ABC, abstractmethod
from random import random
from random import randint

class Spell:
    def __init__(self, name, dang=10, mana=5, type=1) -> None:
        self.name = name

class Hero:
    option1 = True
    points = 0
    spec_points = 0
    level = 1

    def __init__(self, name, health, armor, strong) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    @abstractmethod
    def special_attack(self,other):
        pass

    def attack(self, other):
        l=list(range(1,100))
        print(f"{self.name} attacked {other.name}")
        if random.choice(l) <= 25 and self.spec_points>0:
            print(f"{self.name} use spec attak")
            self.special_attack(other)
            self.spec_points-=1
        else:
            print(f"{self.name} use kick attak")
            self.kick(other)

    def _get_info(self):
        print(
              f"Name {self.name}\n" \
              f"Health - {self.health}\n" \
              f"Armor {self.armor}"
        )
        
    def print_info(self):
         print(self._get_info() + '\n')
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
        if other.health<0:
            self.level+=1
            self.warriors.delete(other)
            

class Mag(Hero):    
    def __init__(self, name, health, armor, strong, mana, spells) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.spells = spells
        self.base_spell = fireball

    def cast_spell(self):
        print(self.base_spell)
    
    def special_attack(self):
        self.cast_spell()


    def print_info(self, sep="-"):
        info =  f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Mana - {self.mana}\n"
        print(info)


class Knight(Hero):
    def __init__(self, name, health, armor, strong ) -> None:
        super().__init__(name, health, armor, strong)


class Arena():
    warriors=[]
    def __init__(self, warriors=[] ) -> None:
        if(len(warriors)>0):
            self.warriors.append(warriors)
        
    def add_warrior(self, warrior):
        if isinstance(warrior,Hero):
            #if list(filter(lambda x:x.name==warrior.name, self.warriors)).count()==0:
                self.warriors.append(warrior)
                print(f"{warrior.name} in battle")
            #else:
                #raise ValueError("warrion on Area")
    
    def choose_warrior(self):
        #return self.warriors[random.randint(0,2)]
        return self.warriors[1]

    def battle(self):
        if len(self.warriors)>1:
            while len(self.warriors)>1:
                attacking=self.choose_warrior()
                defending=self.choose_warrior().delete(attacking)
                attacking.attac(defending)
            winner=self.warriors[0]
            print("The warrior {winner.name} won")
            return winner
        else:
            raise ValueError("The number of warriors in the arena must be more than 1")
          
fireball = Spell('Fireball')        

hero1 = Hero('Dimitri', 50, 20, 15)    
hero2 = Hero('Alex', 60, 10, 5)    
hero3 = Mag('Gendalf', 30, 25, 10, 30, [fireball])    
arena=Arena()
arena.add_warrior(hero1)
arena.add_warrior(hero2)
arena.add_warrior(hero3)
arena.battle()
#print(hero3.base_spell.name)
#hero3.print_info()

#print(hero3.mana)
