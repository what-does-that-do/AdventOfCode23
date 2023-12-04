filename = "Day 2/input.txt"

f = open(filename,'r')
gameColors = ['red','green','blue']

games = []
for line in f.readlines(): # for each game
    game = line.split(':')[0].replace("Game ","") # get id
    rounds = line.split(':')[1].split(';') # get rounds
    print("GAME =",game)
    print("ROUNDS =",rounds)

    allRoundData = []
    for round in rounds: # for each round
        roundData = {}
        colors = round.split(',') # get each color value
        for color in colors: # loop and add to dict
            for c in gameColors:
                if c in color:
                    color = color.replace(c,"").replace(" ","").replace("\n","")
                    roundData[c] = int(color)
        allRoundData.append(roundData)
    games.append(allRoundData)

print(games)
f.close()

id = 1
powers = []
totalPowers = 0

for game in games:
    # Smallest possible values, must be changed on first run.
    red = 0
    green = 0
    blue = 0

    for round in game: # find highest no of each cube in round
        if "red" in round:
            if round["red"] > red:
                red = round["red"]
        if "green" in round:
            if round["green"] > green:
                green = round["green"]
        if "blue" in round:
            if round["blue"] > blue:
                blue = round["blue"]
    
    print("GAME ID",id," - red",red,"green",green,"blue",blue)
    power = red * green * blue # multiply for power
    print("Power =",power)
    '''
    if red <= red_cubes and green <= green_cubes and blue <= blue_cubes: # possible no of cubes
        ids.append(id)
        idTotal += id
        print("[*] = This game fits!")
    else:
        print("[-] = This game does not fit.")
    '''
    powers.append(power)
    totalPowers += power # add to total powers
    id += 1

print(powers)
print("ANSWER:",totalPowers)