from item import Item


class Character:
    def __init__(self, hp):
        self.hp = hp
        self.coins = 0
        self.inventory = []

    def takeDamage(self, damageTaken):
        self.hp = self.hp - damageTaken

    def gainHealth(self, health):
        self.hp = self.hp + health

    def setPlayerHealth(self, health):
        self.hp = health
    
    def getHealth(self):
        return self.hp
    
    def addCoins(self, coins):
        self.coins += coins

    def loseCoins(self, coins):
        self.coins -= coins
    
    def getCoins(self):
        return self.coins

    def addToInventory(self, item: Item):
        self.inventory.append(item)

    def removeFromInventory(self, item:Item):
        self.inventory.remove(item)
    
    def getInventory(self):
        return self.inventory



