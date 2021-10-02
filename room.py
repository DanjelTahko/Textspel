from __future__ import annotations
from enemyCharacter import EnemyCharacter
 
class Room:
    def __init__(self, name):
        self.name = name
        self.toRight = None
        self.toLeft = None
        self.toBack = None
        self.enemyName = None
        self.enemy = None

    def getName(self):
        return self.name

    def setRoomtoRight(self, room: Room):
        self.toRight = room

    def setRoomtoLeft(self, room: Room):
        self.toLeft = room

    def setRoomToBack(self, room: Room):
        self.toBack = room

    def getRoomToRight(self):
        return self.toRight

    def getRoomToLeft(self):
        return self.toLeft

    def getRoomToBack(self):
        return self.toBack

    def setEnemytoRoom(self, enemy: EnemyCharacter):
        self.enemyName = enemy.getName()
        self.enemy = enemy

    def getEnemyInRoomName(self):
        return self.enemyName

    def getEnemy(self):
        return self.enemy