filename = "Day 2/test_case.txt"

f = open(filename,'r')

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
            if "red" in color:
                color = color.replace("red","").replace(" ","")
                roundData["red"] = int(color)
            if "green" in color:
                color = color.replace("green","").replace(" ","")
                roundData["green"] = int(color)
            if "blue" in color:
                color = color.replace("blue","").replace(" ","")
                roundData["blue"] = int(color)
        allRoundData.append(roundData)
    games.append(allRoundData)

f.close()