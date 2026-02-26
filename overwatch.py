'''
Docstring for overwatch
This is a simple overwatch game with hero classes and functions

Test Case Autonation Plan
Author: Jose Orozco
Date: 1/20/2026
Goal: To create a simple overwatch game with hero classes and functions to demonstrate OOP concepts and test case automation
'''


# goal here is to make hero class so that other classes can reference it and we dont have to retype the same code for each hero class
class Hero: 
    def __init__(self, name, health, max_health, ammo, take_damage, ult, is_alive):
        # attribute in hero class cant have the same name as a function 
        # shared logic between all hero classes so we dont retype it all 
        self.name = name 
        # heals done or taken 
        self.health = health
        self.max_health = max_health 
        # damage done or taken 
        self.ammo = ammo
        self.take_damage = take_damage
        # status alive or dead or ult 
        self.ult = ult
        self.is_alive = is_alive
        
    def heal(self, amount):
        self.health += amount # how much amount is healed 
        if self.health > self.max_health: # if max health is less than self health, 
            self.health = self.max_health # this is to cap max health 
        print(f"{self.name} healed to {self.health}")
        
    def damage(self, amount):
        self.health -=amount
        if (self.damage >= self.health):
    

# Tanks to reference main hero class 

class Dva(Hero):
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
        
class Orisa:
    def __init__(self):
        self.name = "Orisa"
        self.damage = float(10.2)
        self.health = 200
        self.ammo = 100
        
    def fire(self):
        if self.ammo > 0:
            print("Orisa fires")
            self.ammo -=1
        else:
            print("Orisa is out of ammo")
            
myOrisa = Orisa()
print(myOrisa.name)
if (Orisa == input("Orisa")):
    print("User is Orisa")
    
            
        
        
myDva = Dva()
print(myDva.name)
print(myDva.ammo)
myDva.fire()
        

# DPS 
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


class Reaper:
    def __init__(self):
        self.name = "Reaper"
        self.health = input("Enter Reaper's health: ")
        self.health = int(self.health)
        
        
class Mei:
    def __init__(self):
        self.name = "Mei"
        self.health = 200
        self.ammo = 100
        

# Support 
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
        
class Kiriko:
    def __init__(self):
        self.name = "Kiriko"
        self.health = 200
        self.ammo = 0
        self.damage = 0
        
        
    def heal(self):
        print("Kiriko heals")
        self.health += 20
        
    def NPCDamage(self):
        print("Kiriko damaages the enemy")
        self.damage += 20
        
    def selfUlt(self):
        print("Kiriko uses her ult")
        self.health += 100
        self.NPCDamage += 100
        
        
    def voiceLine(self):
        noHealthLine = "Has no more health"
        kirikoLine1 = "Kiriko says: I am the fox spirit"
        kirikoLine2 = "Kiriko is healthy"
        print(kirikoLine1)
        if self.health > 200:
            print(kirikoLine2)
        elif self.health <= 200:
            print("Kiriko is not healthy") 
        else:
            print(noHealthLine)
        

myOuterKiriko = Kiriko()
print(myOuterKiriko.name)

myMery = Mercy()
print(myMery.name)

if myMery.health < 100:
    myMery.heal()
else:    myMery.damage()

# class = hero 
# object = a specific hero like Dva or Soldier 76
# functions = actions it can do such as fire, heal, dva boosters, etc
# attributes = health, ammo, name, etc
class JunkerQueen:
    def __init__(self):
        self.name = "Junker Queen"
        self.health = 200
        self.ammo = 100
        self.damage = 0
    
    def damage(self):
        print("Junker Queen damages the enemy")
        self.damage += 20
        self.ammo -= 1
    
    def commandingShout(self):
        print("Junker Queen uses her adrelinene rush")
        self.health =+ 250
        self.speed =+ 5
        
    def rampage(self):
        print("Junker queen is ready to rampage")
        self.damage += 100
        self.speed =+ 50
        

class Moira:
    def __init__(self):
        self.name = "Moria"
        self.health = 200
        self.ammo = 100
        self.damage = 0
        self.numSkins = 10
        self.kills = 0 
        
    def fade(self):
        print('moira fades away')
        self.duration =+ 5
        self.speed =+ 5
        self.max_range = 10
        
    def heal(self):
        print("Moira heals")
        self.health += 20
    
    def damage(self):
        print("Moira damages the enemy")
        self.damage += 20
        self.ammo -= 1
        self.kills += 1
        print("Moria has", self.kills, "kills")
        
    def ult(self):
        print('Moira uses her ult')
        self.health += 100
        self.damage += 100
        self.ammo -= 1
        self.kills =+ 1
        
    def voiceLine(self):
        if self.health > 200:
            voiceLineHeal1 = "Im reborn again"
            print(voiceLineHeal1)
        elif self.health <= 200:
            voiceLineHeal2 = "I must put a stop to their efforts"
            print(voiceLineHeal2)
        else:
            print('Moira has no health')
            voiceLineHeal3 = "Yahhh"
            print(voiceLineHeal3)
            
        
    def skins(self):
        print("Moira has 5 skins")
        if self.numSkins > 5:
            print("Moira has more than 5 skins")
        else:            
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
            
            

###