# Tile Traveller
# E: +1 to x (unless 1,1 eða ef x = 3)
# S: -1 to y (unless 2,3 eða ef y = 1)
# W: -1 to x (unless 3,2 eða ef x = 1)
# N: +1 to y (unless 2,2 eða ef y = 3)

def available_directions(locationx, locationy):
    if locationx == 1:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 3:
            print("You can travel: (E)ast and (S)outh.")
            available = "ES"
        else:
            print("You can travel: (E)ast, (N)orth and (S)outh.")
            available = "ENS"
    elif locationx == 2:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
            print("You can travel: (W)est and (S)outh.")
            available = "WS"
        else:
            print("You can travel: (W)est and (E)ast")
            available = "WE"
    elif locationx == 3:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
            print("You can travel: (N)orth and (S)outh.")
            available = "NS"
        else:
            print("You can travel: (W)est and (S)outh")
            available = "WS"
    
    return available

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

while (locationx != 3) or (locationy != 1):  
  available_directions(locationx, locationy)
  direction = input("Direction: ")
  if direction in available_directions():
    movement = move(direction)
  else:
    print("Not a valid direction!")
