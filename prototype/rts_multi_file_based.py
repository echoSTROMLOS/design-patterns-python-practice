class Knight(object):
    def __init__(self, level):
        self.unit_type = "knight"
        filename = f"{self.unit_type}_{level}.dat"
        with open(filename, "r") as file:
            lines = file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}\n"

class Archer(object):
    def __init__(self, level):
        self.unit_type = 'archer'
        filename = f"{self.unit_type}_{level}.dat"
        with open(filename, "r") as file:
            lines = file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4] 

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
  