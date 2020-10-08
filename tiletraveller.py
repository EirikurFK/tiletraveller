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
        elif locationy == 2:
            pull_lever(coin_count)
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            available = "ENS"
        elif locationy == 3:
            print("You can travel: (E)ast or (S)outh.")
            available = "ES"
    elif locationx == 2:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
            pull_lever(coin_count)
            print("You can travel: (S)outh or (W)est.")
            available = "WS"
        else:
            pull_lever()
            print("You can travel: (E)ast or (W)est.")
            available = "WE"
    elif locationx == 3:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
            pull_lever()
            print("You can travel: (N)orth or (S)outh.")
            available = "NS"
        else:
            print("You can travel: (S)outh or (W)est.")
            available = "WS"
    
    return available


def pull_lever(coin_count):
    pull_lever = input("Pull a lever (y/n): ").upper()
    if pull_lever == "Y":
        coin_count = get_coin(coin_count)

    return coin_count


def get_coin(coin_count):
    coin_count += 1
    print("You received {} coin, your total is now {}.".format(1, coin_count))

    return coin_count

    

  


def move(direction, locationx, locationy):
    if direction == "E":
        locationx += 1
        return locationx
    elif direction == "W":
        locationx += -1
        return locationx
    elif direction == "S":
        locationy += -1
        return locationy
    elif direction == "N":
        locationy += 1
        return locationy

locationx = 1
locationy = 1
coin_count = 0

while True:
    directions = available_directions(locationx, locationy)
    direction = input("Direction: ")
    direction = direction.upper()

    if direction in directions:
        if direction == "E" or direction == "W":
            locationx = move(direction, locationx, locationy)
        else:
            locationy = move(direction,locationx, locationy)
    else:
        print("Not a valid direction!")

    if locationx == 3 and locationy == 1:
        print("Victory! Total coins {}.".format(coin_count))
        break