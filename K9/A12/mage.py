import random


class Mage:
    def __init__(self):
        self.initiative = random.randint(1, 6)
        self.live = random.randint(1, 6)
        self.charged = False
        self.heal = False
        self.noDamage = 0

    def fireball(self):
        damage = random.randint(2, 7)
        print("Damage: ", damage)
        return damage

    def magicMissile(self):
        damage = random.randint(1, 6)
        print("Damage: ", damage)
        return damage

    def mirrorImages(self):
        rand = random.randint(1, 2)
        if (rand == 1):
            self.noDamage = 2
            print("No Damage for tow rounds")
        else:
            print("Fail")

    def smallhealing(self):
        healing = random.randint(1, 4)
        self.live = self.live+healing
        print("Character healing ", healing)

    def attack(self):
        while (True):
            choise = input(
                "Which Attack? (1=Fireball, 2=MagicMissile, 3=MirrorImage, 4=SmallHealing): ")
            if (choise == "1"):
                if (self.charged == True):
                    self.fireball()
                    self.charged = False
                    break
                else:
                    print("Fireball is charged")
                    self.charged = True
                    break
            if (choise == "2"):
                self.magicMissile()
                break
            if (choise == "3"):
                self.mirrorImages()
                break
            if (choise == "4"):
                if (self.heal == False):
                    self.heal = True
                    self.smallhealing()
                    break
                else:
                    print("Healing allready used")
            print("Wrong Input")
