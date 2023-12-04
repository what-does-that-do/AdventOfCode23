file = "Day 4/input.txt"
f = open(file,'r')

numbers = []
for line in f.readlines():
    text = line.split(':')[1].strip().replace('\n','')
    myNumbers = text.split('|')[1].split(' ')
    winningNumbers = text.split('|')[0].split(' ')
    numbers.append([winningNumbers,myNumbers])
f.close()

totalPoints = 0
for Set in numbers:
    points = 0
    for win in Set[0]:
        if win == '':
            continue
        if win in Set[1]:
            if points >= 1:
                points *= 2
            else:
                points = 1
    totalPoints += points

print("Points =",totalPoints)