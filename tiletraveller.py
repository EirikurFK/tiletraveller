# Tile Traveller
# E: +1 to x (unless 1,1 eða ef x = 3)
# S: -1 to y (unless 2,3 eða ef y = 1)
# W: -1 to x (unless 3,2 eða ef x = 1)
# N: +1 to y (unless 2,2 eða ef y = 3)
import random

LEVER_POSITIONS = [[1,2],[2,2],[2,3],[3,2]]

def get_random_direction():
    direction = random.choice(["N", "E", "S", "W"])
    return direction

def get_random_lever_pull():
    pull_lever = random.choice(["Y", "N"])
    return pull_lever

def available_directions(locationx, locationy):
    if locationx == 1:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
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
            print("You can travel: (S)outh or (W)est.")
            available = "WS"
        else:
            print("You can travel: (E)ast or (W)est.")
            available = "WE"
    elif locationx == 3:
        if locationy == 1:
            print("You can travel: (N)orth.")
            available = "N"
        elif locationy == 2:
            print("You can travel: (N)orth or (S)outh.")
            available = "NS"
        else:
            print("You can travel: (S)outh or (W)est.")
            available = "WS"
    
    return available


def pull_lever(coin_count):
    # pull_lever = input("Pull a lever (y/n): ").upper()
    pull_lever = get_random_lever_pull()
    print("Pull a lever (y/n):", pull_lever.lower())
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

def play():
    locationx = 1
    locationy = 1
    coin_count = 0
    moves = 0
    previous_location = []
    while True:
        current_location = [locationx, locationy]
        if current_location != previous_location:
            for position in LEVER_POSITIONS:
                if locationx == position[0]:
                    if locationy == position[1]:
                        coin_count = pull_lever(coin_count)

        directions = available_directions(locationx, locationy)
        # direction = input("Direction: ")
        # direction = direction.upper()
        direction = get_random_direction()
        print("Direction:", direction.lower())
        previous_location = [locationx, locationy]
        
        if direction in directions:
            if direction == "E" or direction == "W":
                locationx = move(direction, locationx, locationy)
            else:
                locationy = move(direction,locationx, locationy)
        else:
            print("Not a valid direction!")
        
        moves += 1

        if locationx == 3 and locationy == 1:
            print("Victory! Total coins {}. Moves {}.".format(coin_count, moves))
            break

# LEVER_POSITIONS = [[1,2][2,2][2,3],[3,2]]
proceed = "Y"
while proceed == "Y":
    input_seed = int(input("Input seed: "))
    random.seed(input_seed)
    play()
    proceed = input("Play again (y/n): ").upper()