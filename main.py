from room import Room
from item import Item
import random


def createWorld():
    bar = Room("Bar")
    firstRoom = Room("Room 1")
    secondRoom = Room("Room 2")
    thirdRoom = Room("Room 3")
    toilet = Room('Toilet')

    bar.setRoomtoRight(firstRoom)  # second room is right of first room
    bar.setRoomtoLeft(toilet)
    toilet.setRoomToBack(bar)
    firstRoom.setRoomtoRight(toilet)
    firstRoom.setRoomtoLeft(secondRoom)

    secondRoom.setRoomtoLeft(thirdRoom)
    secondRoom.setRoomtoRight(bar)
    bar.setRoomToBack(secondRoom)
    secondRoom.setRoomToBack(firstRoom)
    # plains.setRoomToTheSouth(forest) # forest is south of plains
    # forest.setRoomToTheWest(toilet)

    return bar  # return the starting location


def printPlayerState(currentRoom: Room):
    print("----------")  # a separator line between player turns
    print("Location: " + currentRoom.getName())


def printPlayerChoises(currenRoom: Room):
    if currenRoom.getName() == "Room 1":
        print('Choises: go right/go left')
    elif currenRoom.getName() == "Room 2":
        print('Choises: go right/go left/go back')
    elif currenRoom.getName() == "Toilet":
        print('Choises: use toilet/go back')


def getRoomInDirection(currentRoom: Room, direction):
    if direction == "right":  # the player wants to move right
        return currentRoom.getRoomToRight()
    elif direction == "left":  # the player wants to move left
        return currentRoom.getRoomToLeft()
    elif direction == "back":  # the player wants to move back
        return currentRoom.getRoomToBack()


currentRoom = createWorld()


keepPlaying = True
while keepPlaying:
    printPlayerState(currentRoom)
    printPlayerChoises(currentRoom)

    command = input("What do you wish to do? ")
    subcommands = command.split(" ")  # split “go” and “right”

    if subcommands[0] == "go":  # the player wants to move
        newRoom = getRoomInDirection(currentRoom, subcommands[1])
        if newRoom == None:
            print("You are unable to move further " + subcommands[1])
        else:
            currentRoom = newRoom  # perform the actual move

    
