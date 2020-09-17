# Tile Traveller

def move(direction):
    if direction == "e":
        locationx += 1
        return locationx
    elif direction == "w":
        locationx += -1
        return locationx
    elif direction == "n":
        locationy += -1
        return locationy
    elif direction == "s":
        locationy += -1
        return locationy

locationx = 1
locationy = 1


while location != 3,1:

dircetion = input("Direction: ")

movement = move(direction)