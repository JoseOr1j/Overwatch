# main hero class that defines everything for the other classes 

class Cosmetics:
    def __init__(self, skin, emote, voice_line, cost):
        self.skin = skin
        self.emote = emote
        self.voice_line = voice_line
        self.cost = cost 
    
class Rank:
    def __init__(
        self, tier, division, points
        
    ):
        self.tier = tier
        self.division = division
        self.points = points
        
        
class BattlePass:
    def __init__(self, level, exp, rewards, test):
        self.tier = self.tier
        self.level = level
        self.exp = exp
        self.rewards = rewards
        
        
class Weapon:
    def __init__(self, ammo, damage, fire_rate, reload_time):
        self.ammo = ammo
        self.damage = damage
        self.fire_rate = fire_rate
        self.reload_time = reload_time
        
    def shoot(self):
        if self.ammo <= 0:
            print("Out of ammo, reloading")
            self.reload()
            return False
        self.ammo -= 1
        print(f"Shot fired! Ammo left: {self.ammo}")
        return True
    
    def reload(self):
        print("Reloading... Please wait.")
        self.ammo = 30 
        # depends on the hero 
        
        
class Map:
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        
    def start_match(self):
        print("Starting m,atch on", self.name)
        
    def end_match(self):
        print("Match ended on", self.name)
        
    def calc_winner(self, team1_score, team2_score):
        if team1_score > team2_score:
            return "Team 1 wins!"
        elif team2_score > team1_score:
            return "Team 2 wins!"
        else:
            return "It's a tie!"
        
    
    
class Endorsement:
    def __init__(self, level):
        self.level = level
        
    def endorsementCheck(self):
        if (Endorsement.level > 0):
            print("Endorsement is to low")
            
        elif (Endorsement.level < 0):
            print("Endorsement is above 0, voice chat is allowed")
            
        else:
            print("Not avaliable banned or other status")
        

class Hero:
    def __init__(
        self,
        name,
        role,
        max_health,
        speed,
        ammo,
        damage_per_shot,
        healing_per_use,
    ):
        self.name = name
        self.role = role
        self.max_health = max_health
        self.health = max_health
        self.speed = speed
        self.ammo = ammo
        self.damage_per_shot = damage_per_shot
        self.healing_per_use = healing_per_use
        self.ultimate_charge = 0

    def is_alive(self):
        return self.health > 0

    def ultimate_ready(self):
        return self.ultimate_charge >= 100

    def take_damage(self, amount):
        if amount < 0:
            amount = 0
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount=None):
        if amount is None:
            amount = self.healing_per_use
        if amount < 0:
            amount = 0

        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def shoot(self):
        if self.ammo <= 0 or not self.is_alive():
            return False

        self.ammo -= 1
        self.gain_ultimate(4)
        return True

    def gain_ultimate(self, amount):
        if amount < 0:
            amount = 0

        self.ultimate_charge += amount
        if self.ultimate_charge > 100:
            self.ultimate_charge = 100

    def use_ultimate(self):
        if not self.ultimate_ready() or not self.is_alive():
            return False

        self.ultimate_charge = 0
        return True


# dva class is one of the classes we can create that inherits from Hero and adds specific behaviors for D.Va, such as boosters and self-destruct.
class Dva(Hero):
    """Example hero that reuses Hero behavior and adds D.Va actions."""

    def __init__(self):
        super().__init__(
            name="D.Va",
            role="Tank",
            max_health=650,
            speed=5.5,
            ammo=60,
            damage_per_shot=2,
            healing_per_use=0,
        )
        self.in_mech = True

    def boosters(self):
        if not self.is_alive():
            return "D.Va cannot use boosters while eliminated."
        return "D.Va uses Boosters!"

    def self_destruct(self):
        if self.use_ultimate():
            self.in_mech = False
            return "NERF THIS! (Self-Destruct activated)"
        return "Ultimate not ready."
    
    class Zarya(Hero):
        #Example of Zaryas functions#
         def __init__(self):
             super().__init__(
                 name = "Zarya", 
                 role = "Tank", 
                 max_health= 400, 
                 speed = 5.5,
                 ammo = 60,
                 damage_per_shot = 2,
                 healing_per_use = 0
             )
             self.energy = 0
             
            ''' def particle_barrier(self):
                if not self.is_alive():
                    return "Zarya cannot use particle barrier"
                return "Zarya uses particle barrier" '''
        


# main function to actually test the Dva class and its methods
if __name__ == "__main__":
    dva = Dva()
    print(dva.name, "| HP:", f"{dva.health}/{dva.max_health}", "| Ult:", f"{dva.ultimate_charge}%")

    for _ in range(10):
        dva.shoot()

    dva.take_damage(120)
    dva.gain_ultimate(65)

    print("After combat -> HP:", dva.health, "Ammo:", dva.ammo, "Ult:", f"{dva.ultimate_charge}%")
    print(dva.boosters())
    print(dva.self_destruct())