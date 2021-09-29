from __future__ import annotations
import random


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

    def getEnemyInRoom(self):
        return self.enemyName

    def getEnemy(self):
        return self.enemy


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

    def whatCanThisBe(self):
        return 'tacobaco'


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

    def gainCoins(self, coins):
        self.coins += coins

    def loseCoins(self, coins):
        self.coins -= coins

    def getCoins(self):
        return self.coins
