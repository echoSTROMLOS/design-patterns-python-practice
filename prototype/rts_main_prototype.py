from prototype_1 import Prototype 
from copy import deepcopy 

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = 'knight'
        filename = f"{self.unit_type}_{level}.dat"

        with open(filename, 'r') as file:
            lines = file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}\n"
    
    def clone(self):
        return deepcopy(self)
        

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = 'archer'
        filename = f"{self.unit_type}_{level}.dat"

        with open(filename, 'r') as file:
            lines = file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}\n"
    
    def clone(self):
        return deepcopy(self)
    

class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()
    

if __name__ == "__main__":
    import time
    x = time.time()
    barracks = Barracks()
    knight1 = barracks.build_unit('knight', 1)
    archer2 = barracks.build_unit('archer', 2)
    print(f"[knight1] {knight1}")
    print(f"[archer2] {archer2}")
    y = time.time()
    print("elapsed_time", y-x)


