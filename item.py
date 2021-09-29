
from random import random
import random


class Item:
    def __init__(self, name):
        self.name = name
        self.damage = None
        

    def getItem(self):
        return self.name

    def setDamage(self, damage):
        self.damage = random.randint(0, damage)
        return self.damage
    
    def getDamage(self):
        return self.damage

