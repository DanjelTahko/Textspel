class Character:
    def __init__(self, hp):
        self.hp = hp
        self.coins = 0

    def getHealth(self):
        return self.hp

    def takeDamage(self, damageTaken):
        self.hp = self.hp - damageTaken

    def gainHealth(self, health):
        self.hp = self.hp + health

    def setPlayerHealth(self, health):
        self.hp = health
    
    def addCoins(self, coins):
        self.coins += coins

    def loseCoins(self, coins):
        self.coins -= coins
    
    def getCoins(self):
        return self.coins

   
