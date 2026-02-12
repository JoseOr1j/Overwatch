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
            
        
    def isAlive(self, health):
        if self.health > 0:
            self.is_alive = True
        else:
            self.is_alive = False
        
    

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
        
# Tanks to reference main hero class 
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
""" ==============================
Things to do:
STAR method
Ask follow up questions 

QA questions: 

q: How can you test a pencil:
I would test the material it is made out of for the durability 
I would test writing with it on various surfaces like paper or wood
I would test its durability by snapping, dropping, or throwing it
I would test if the eraser works
I would test if it is able to be rolled
If it is able to be sharpened 

q: Black Box testing
Black box is when you are testing the functions of the device without knowing
how it works for example testing fyi app without knowing the code but testing the functionality 
of the app

q: White box testing 
White box is when you are testing the functions of a device but you know how it work and access
to the code, testing if things such as inner functions work ie:
def add(a,b): works on the backend of the code but not necessarily the frontend of the code (UI)
Which is why we have the black box testing

q: How would you find when a bug occured on a build?
for example we found a regression on build 100, how would you find when the bug was introduced?
Ans: Divide and Conquer, if its on build 100 i would start on build 50 and test if
it exisst there, if it does then i would go to build 25 and test 
and so on and so forth splitting each by half until i find the build where the bug was introduced.

q: What is the SDLC?
ans: the SDLC is the software dev lifecycle 
this is the cycle in which software is created 
usually starts with the plan to develop a piece of software (business/idea)
then moves to the creation of the software which gets iterated in sprints
software that is then created gets tested in the QA process for bugs, if a bug is found sent to engineer 
software reverts back for development unitl it is completed
once completed it is in the cycle to redevlop and change (maintain it)

q: What is test automation and why is it important?
ans: test automation is important because it helps save time and costs which are associated with manual testing
an example of a test case that can be automated would be mundane or easier tasks which do not require any human opinion or exploratory testing
such as logging in to a website or app 
something that is usually run various times per day or build would be important to automate 
Automation is used to maximize ROI 

q: What is the STLC?
The STLC is the cycle in which software is tested 
Starts with a test plan for what will be tested and includes the description of what will be done and the goal 
ie: Test functions of FYI app will test the app login 
then a test case is created around to those test plans to ensure each part of the app is tested 
once this is created usually on a bug or test case tracker like JIRA it is then tested 

q: What is a bug?
A bug is an issue that is found in a piece of software or hardware
In QA a bug is any problem that impacts the functionality of the software 
A bug has a variety of severity levels on JIRA such as low/mid/high/blocker 
UI issues/text errors are usually low 
Middle is usually issues that are harder to reproduce 
High are issues which affect a large component of the apps functionality, but app still works
Blockers are issues which cease the apps functionality and must be addressed before moving to new builds or itertaions 

q: What is a regression?
A regression is an issue/bug that has returned on a new build of the software 
ie bug 101 was found on build 20 and was fixed on build 23
but then bug 101 was found again on build 33 later on, that is a regression bc the bug regressed 

q: what is unit testing ?
unit testing is usually associated with white box testing 
involves testing units of an app as individuals rather than as a whole system
so this involves testing pieces of code to ensure that each function or unit works properly 
looks like 
assert (xyz) == "xyz"
assert (lol) = "lol"

q: How to categorize a bugs severity on JIRA?
A bugs severity levels depend on how much a bug impacts the function of an app 
If a bug is a UI issue which impacts something like a login, that is usually high priority to fix if it impacts the login directly
If the bug is an issue where the backend authentciation for login fails and no user can login that is usually a severe bug also known as a blocker and 
must be fixed before any new builds are introduced to the public 

q: write a sample test case?
Test Case 1: 
[AI, iOS] Ensure that AI voicechat works
Enviornment iOS, Operating System: iOS 26, Build 100
Expected behavior: P1 should be able to talk to the AI using audio voicechat and text 
Preconditions: 
Steps to reproduce:
P1 is in the apps homescreen
P1 taps on the "AI" hometab and is lead to the AI chatbot screen
P1 taps on the voicechat option 
P1 taps on the audio button and taps to speak
! P1 should be able to talk to the AI 
Expected behavior is etc etc
Attachments on JIRA: Videos or Photos

q: What is the difference between functional and non functional testing? 
Functional testing has to do with testing based on business requirments such as "does the login work?", "does the AI chatbot work?"
Non-Functional testing has to do with testing things that are not required such as "time it takes to login", "How fast does the AI chatbot respond?", "how many queries?"

q: What is an API? 
An application program interface is used in order to communicate information from the backend to the frontend of an app
for example an API for the weather can be written in JS backend to access that info on the HTML/CSS frontend 

q: what is version control?
Version control is the ability to work on different branches of work in software
An example of this would be git and github
Git is used to push and pull changes from a repository which includes work of software 
If a build were to be pushed to a "master" build it updates for everyone else 
If you were to pull your changes and you are behind it will merge those existing changes 

q: explain the different types of testing 
Functional: Does the login work?
Non Functional: How fast does it login?
Regression: The bug that was fixed, came back reappeared in a new build 
Ad-Hoc: Fun but with a purpose 
Exploratory: Even more fun, just random testing
Stress: What is the number of users the server load can take before the app shuts down 
Compatibility: Localization, currency, language, cultural 



====================== """ 

###