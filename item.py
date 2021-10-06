import random


class Item:
    def __init__(self, name, minDamage, maxDamage):
        self.name = name
        self.damage = None
        self.maxDamage = maxDamage
        self.minDamage = minDamage

    def getItem(self):
        return self.name

    def setDamage(self):
        self.damage = random.randint(self.minDamage, self.maxDamage)
        return self.damage

    def getDamage(self):
        return self.damage
    
    def getMaxDamage(self):
        return self.maxDamage

    # Ett fusk som är avstängt atm
    def whatCanThisBe(self):
        return 'tacobaco'