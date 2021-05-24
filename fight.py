import random
from time import sleep


f1_lvl, f2_lvl = random.randint(0, 5), random.randint(0,5)


f1_data = {
    "member": {
        "id": 8253286226541,
        "name": "Kenshi",
    },

    "specs": {
        "lvl": f1_lvl,
        "hp": 100 + f1_lvl*10,
        "exp": 0,
        "crt": 10 + f1_lvl*5,
        "dmg": 20 + int(f1_lvl*1.2),
    },

    
}


f2_data = {
    "member": {
        "id": 81240125489,
        "name": "Sange",
    },

    "specs": {
        "lvl": f2_lvl,
        "hp": 100 + f2_lvl*10,
        "exp": 0,
        "crt": 10 + f2_lvl*5,
        "dmg": 20 + int(f2_lvl*1.2),
    },

    
}

class Fighter():

    def __init__(self,member:dict, specs:dict):
        self.__member = member
        self._specs = specs
        self.__new_specs = specs
        self.can_fight = True

    def attack(self, target:"Fighter"=None):
        attack_chance = random.randint(0,f1._specs["dmg"])
        crit_chance = random.randint(1,100)

        if attack_chance > 0:
            if crit_chance > 20:
                target._specs["hp"] -= self._specs["dmg"]
            else:
                target._specs["hp"] -= self._specs["dmg"] + self._specs["crt"]
        else:
            target._specs["hp"] -= 0

        if target._specs["hp"] <=0:
            target.can_fight = False

    def win(self, target:"Fighter"=None):
        diff = abs(self._specs["lvl"] - target._specs["lvl"])

        if diff < 4:
            self._specs["exp"] += 10
        elif diff < 9:
            if self._specs["lvl"] > target._specs["lvl"]:
                self._specs["exp"] -= 5
            else:
                self._specs["exp"] += 20

        elif diff > 9:

            if self._specs["lvl"] > target._specs["lvl"]:
                self._specs["exp"] -= 40
            else:
                self._specs["exp"] += 80

        if self._specs["exp"] >=100:
            self.__lvl_up()

    def __lvl_up__(self):
        pass
    
    def __str__(self):
        return f"Боец {self.__member['name']} имеет параметры {self._specs}"


f1 = Fighter(f1_data["member"], f1_data["specs"])
f2 = Fighter(f2_data["member"], f2_data["specs"])

print(f1)
print(f2)


        


def fight(f1:"Fighter" = None, f2:"Fighter"=None):
    
    turn = True

    while f1.can_fight and f2.can_fight:
        sleep(2)

        if turn:
            turn = False
            f1.attack(f2)

        else:
            turn = True
            f2.attack(f1)

   


    if f1.can_fight:
        f1.win(f2)
        print(f"{f1.name} победил {f2.name} и имеет {f1.hp} здоровья")
    else:
        f2.win(f1)
        print(f"{f2.name} победил {f1.name} и имеет {f1.hp} здоровья")
        

fight(f1,f2)