class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"
        if level == 1:
            self.life = 500
            self.speed = 7 
            self.attack_power = 4 
            self.attack_range = 1
            self.weapon = "Short Battle Sword" 
        elif level == 2:
            self.life = 500
            self.speed = 7 
            self.attack_power = 7
            self.attack_range = 2
            self.weapon = "Long Battle Sword"

    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}\n"

class Archer(object):
    def __init__(self, level):
        self.unit_type = 'Archer'
        if level == 1:
            self.life = 200
            self.speed = 10
            self.attack_power = 2
            self.attack_range = 5
            self.weapon = "Short Bow" 
        elif level == 2:
            self.life = 200
            self.speed = 10 
            self.attack_power = 4
            self.attack_range = 10
            self.weapon = "Long Bow" 

    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}\n"


class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == 'knight':
            return Knight(level)
        elif unit_type == 'archer':
            return Archer(level)
        
    

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit('knight', 1)
    archer2 = barracks.build_unit('archer', 2)
    print(f"[knight1] {knight1}")
    print(f"[Archer2] {archer2}")