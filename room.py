from __future__ import annotations
 
class Room :
    def __init__(self, name) :
        self.name = name
        self.toNorth = None
        self.toSouth = None
        self.toWest = None
        self.toEast = None
 
    def getName(self) :
        return self.name
 
    def setRoomtoRight(self, room: Room) :
        self.toNorth = room
    def setRoomtoLeft(self, room: Room) :
        self.toSouth = room
    def setRoomToBack(self, room: Room) :
        self.toEast = room
 
    def getRoomToRight(self) :
        return self.toNorth
    def getRoomToLeft(self) :
        return self.toSouth
    def getRoomToBack(self) :
        return self.toEast


  
