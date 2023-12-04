file = "Day 4/input.txt"
f = open(file,'r')

numbers = []
lines = 0
for line in f.readlines():
    text = line.split(':')[1].strip().replace('\n','')
    myNumbers = text.split('|')[1].split(' ')
    winningNumbers = text.split('|')[0].split(' ')
    numbers.append([winningNumbers,myNumbers])
    lines += 1
f.close()

cardInfo = {}
for set in numbers:
    wins = 0
    for win in set[0]:
        if win == '':
            continue
        if win in set[1]:
            wins += 1
    if set in cardInfo:
        instances = cardInfo[set]
    for win in range(wins):
        if cardInfo[int(set) + win] in cardInfo:
            cardInfo[int(set) + win] = cardInfo[int(set) + win] + 1
        else:
            cardInfo[int(set) + win] = 1

totalCards = 0
for c in cardInfo:
    if c < lines:
        totalCards += cardInfo[c]