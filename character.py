class Character :
    def __init__ (self, hp) :
        self.hp = hp

    def getHealth(self) :
        return self.hp
    
    def takeDamage(self, damageTaken):
        self.hp = self.hp - damageTaken
