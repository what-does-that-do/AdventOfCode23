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

red_cubes = 12
green_cubes = 13
blue_cubes = 14

id = 1
ids = []
idTotal = 0
for game in games:
    red = 0
    green = 0
    blue = 0

    definetelyNot = False

    for round in game: # count up total red,green,blue cubes of round
        if "red" in round:
            if round["red"] > red_cubes:
                definetelyNot = True
        if "green" in round:
            if round["green"] > green_cubes:
                definetelyNot = True
        if "blue" in round:
            if round["blue"] > blue_cubes:
                definetelyNot = True
    
    print("GAME ID",id," - red",red,"green",green,"blue",blue)
    print(game)
    if definetelyNot:
        print("[-] Does not work")
    else:
        print("[+] Works")
        ids.append(id)
        idTotal += id

    '''
    if red <= red_cubes and green <= green_cubes and blue <= blue_cubes: # possible no of cubes
        ids.append(id)
        idTotal += id
        print("[*] = This game fits!")
    else:
        print("[-] = This game does not fit.")
    '''

    id += 1

print(ids)
print("ANSWER:",idTotal)
