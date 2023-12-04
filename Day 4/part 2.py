file = "Day 4/test_case.txt"
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
i = 0
for Set in numbers:
    if i in cardInfo:
        instances = cardInfo[i]
    else:
        instances = 1
    print(instances,"of scratchcard",i)
    for x in range(instances):
        wins = 0
        for win in Set[0]:
            if win == '':
                continue
            if win in Set[1]:
                wins += 1
        print(wins,"wins")


        for win in range(wins):
            if int(i) + win + 1 in cardInfo:
                cardInfo[int(i) + win+1] = cardInfo[int(i) + win + 1] + 1
            else:
                cardInfo[int(i) + win + 1] = 1
            print("Added 1 to",i+win+1)
    i += 1

totalCards = 0
for c in cardInfo:
    if c < lines:
        totalCards += cardInfo[c]

print("Total cards =",totalCards)