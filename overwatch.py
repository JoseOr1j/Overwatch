def heroClass (hero):
    if hero == "dva":
        print ("the selected class is dva")
    elif hero == "genji":
        print ("the selected class is genji")
    else:
        print("the selecteed class is: ", hero)

heroClass("genji")

# fizzbuzz

for i in range(1, 101):
    # start at 1 and then go to 2 and 3 and so on until 101
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:        print("none")
    
    
    for i in range(1,6):
        print("dvaLoop", i)
        

class Dva:
    def __init__(self):
        self.name = "DVA"
        self.ammo = 100
        self.health = 600
        self.in_mech = True
    
    def fire(self):
        if self.ammo > 0:
            print("Dva fires")
            self.ammo =-1
        else:
            print("Dva is out of ammo")
        
    def boosters(self):
        print("booster")
        
        
myDva = Dva()
print(myDva.name)
print(myDva.ammo)
myDva.fire()
        


class Soldier76:
    def __init__(self):
        self.name = "Soldier 76"
        self.ammo = 100
        self.health = 200
        
    def fire(self):
        if self.ammo >0:
            print("Soldier fires")
            self.ammo -=1
        else:
            print("Soldier is out of ammo")
            
            
outsideSoldier = Soldier76()
print(outsideSoldier.name)

class Mercy:
    def __init__(self):
        self.name = "Mercy"
        self.health = 200
        self.enemyHealth = 200
        self.ammo = 0
        
    def heal(self):
        print("Mercy heals")
        health+=20
        
    def damage(self):
        print("Mercy damages")
        enemyHealth-=20

myMery = Mercy()
print(myMery.name)

if myMery.health < 100:
    myMery.heal()
else:    myMery.damage()

# class = hero 
# object = a specific hero like Dva or Soldier 76
# functions = actions it can do such as fire, heal, dva boosters, etc
# attributes = health, ammo, name, etc

class Moira:
    def __init__(self):
        self.name = "Moria"
        self.health = 200
        self.ammo = 100
        self.damage = 0
        self.numSkins = 10
        self.kills = 0 
        
    def heal(self):
        print("Moira heals")
        self.health += 20
    def damage(self):
        print("Moria uses her ult")
        self.ammo -= 100
        self.damage += 100
        
    def skins(self):
        print("Moira has 5 skins")
        if self.numSkins > 5:
            print("Moira has more than 5 skins")
        else:            p
        print("Moira has less than 5 skins")
    
    def kills(self):
        isDead = False
        print("Moria has", self.kills, "kills")
        if self.kills > 10:
            print("Moria has more than 10 kills")
        elif self.kills <= 10:
            print("Moria has less than or equal to 10 kills")
        elif self.isDead == True:
            print("Moria is dead")
        else:
            print("Moira has no kills")
            
        
        