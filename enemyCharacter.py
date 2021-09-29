class EnemyCharacter:
    def __init__ (self, hp, damage):
        self.hp = hp
        self.damage = damage

    def getHealth(self) :
        return self.hp
    
    def takeDamage(self, damageTaken):
        self.hp = self.hp - damageTaken

    def getDamage(self):
        return self.damage