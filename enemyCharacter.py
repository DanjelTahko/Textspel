import random

class EnemyCharacter:
    def __init__(self, name, hp, minDamage, maxDamage):
        self.name = name
        self.hp = hp
        self.damage = None
        self.maxDamage = maxDamage
        self.room = None
        self.minDamage = minDamage

    def getHealth(self):
        return self.hp

    def takeDamage(self, damageTaken):
        self.hp = self.hp - damageTaken

    def setDamage(self):
        self.damage = random.randint(self.minDamage, self.maxDamage)
        return self.damage

    def getDamage(self):
        return self.damage

    def getName(self):
        return self.name