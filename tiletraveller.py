# Tile Traveller
# E: +1 to x (unless 1,1 eða ef x = 3)
# S: -1 to y (unless 2,3 eða ef y = 1)
# W: -1 to x (unless 3,2 eða ef x = 1)
# N: +1 to y (unless 2,2 eða ef y = 3)

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

def available_directions(locationx, locationy):
    if locationx == 1:
        if locationy == 1:
            print("You can travel: (N)orth.")
        elif locationy == 3:
            print("You can travel: (E)ast and (S)outh.")
        else:
            print("You can travel: (E)ast, (N)orth and (S)outh.")
    elif locationx == 2:
        if locationy == 1:
            print("You can travel: (N)orth.")
        elif locationy == 2:
            print("You can travel: (W)est and (S)outh.")
        else:
            print("You can travel: (W)est and (East)")





locationx = 1
locationy = 1


while location != 3,1:

direction = input("Direction: ")

movement = move(direction)