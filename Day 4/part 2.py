file = "Day 4/input.txt"
f = open(file,'r')

numbers = []
lines = 0

# Format lines
for line in f.readlines():
    text = line.split(':')[1].strip().replace('\n','')
    myNumbers = text.split('|')[1].split(' ')
    winningNumbers = text.split('|')[0].split(' ')
    numbers.append([winningNumbers,myNumbers])
    lines += 1
f.close()

cardInfo = {}
i = 0
totalCards = 0

for Set in numbers:
    if i in cardInfo:
        instances = cardInfo[i]
    else:
        instances = 1
    print("**",instances,"of scratchcard",i)
    totalCards += instances
    for x in range(instances): # repeat for each scratchcard
        # Find number of wins
        wins = 0
        for win in Set[0]:
            if win == '':
                continue
            if win in Set[1]:
                wins += 1
        #print(wins,"wins")

        # Add number of instances of card to dict
        for win in range(wins):
            if int(i) + win + 1 in cardInfo:
                cardInfo[int(i) + win+1] = cardInfo[int(i) + win+1] + 1
            else:
                cardInfo[int(i) + win+1] = 2
            #print("Added 1 to",int(i)+win+1)
    i += 1

print("Total cards =",totalCards)