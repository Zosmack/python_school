import random


class Warrior:
    def __init__(self):
        self.initiative = random.randint(1, 8)
        self.live = random.randint(1, 10)
        self.heal = False

    def swordstroke(self):
        damage = random.randint(1, 7)
        print("Damage: ", damage)
        return damage

    def schieldblock(self):
        schield = random.randint(1, 4)
        print("Next Attack decrease by", schield)
        self.live = self.live+schield

    def healthpotion(self):
        healing = random.randint(1, 6)
        self.live = self.live+healing
        print("Character healing ", healing)

    def attack(self):
        while (True):
            choise = input(
                "Which Attack? (1=SwordStroke, 2=SchieldBlock, 3=Healthpotion): ")
            if (choise == "1"):
                self.swordstroke()
                break
            if (choise == "2"):
                self.schieldblock()
                break
            if (choise == "3"):
                if (self.heal == False):
                    self.heal = True
                    self.healthpotion()
                    break
                else:
                    print("Healing allready used")
            print("Wrong Input")
