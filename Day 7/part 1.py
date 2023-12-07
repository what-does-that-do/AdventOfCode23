file = "Day 7/test_case.txt"
f = open(file,'r')

cards = [[],[]] # [type], [bid]
ranks = {}
rankOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cardChars = []

for line in f.readlines():
    l = line.replace('\n','').split(" ")
    cards[0].append(l[0])
    cards[1].append(l[1])
    cc = {}
    for r in rankOrder:
        cc[r] = l[0].count(r)
    cardChars.append(cc)

print(cards)
print(cardChars)

cardStrengths = []
strengths = {}

for i in range(len(cards[0])):
    chars = cardChars[i]
    highest = 0
    nHighest = 0

    for c in chars:
        if int(chars[c]) > highest:
            highest = int(chars[c])
            nHighest = 0
        if int(chars[c]) == highest:
            nHighest += 1
    #roll out format below!
    if highest == 1:
        if "High card" in strengths:
            s = strengths['High card'] 
            s.append(cards[0][i])
            strengths['High card'] = s
        else:
            strengths['High card'] = [cards[0][i]]
    elif highest == 2:
        if nHighest == 1:
            strengths['One pair'] = cards[0][i]
        else:
            strengths['Two pair'] = cards[0][i]
    elif highest == 3:
        two = False
        for c in chars:
            if int(chars[c]) == 2:
                two = True
        if two:
            strengths['Full house'] = cards[0][i]
        else:
            strengths['Three of a kind'] = cards[0][i]
    elif highest == 4:
        strengths['Four of a kind'] = cards[0][i]
    elif highest == 5:
        strengths['Five of a kind'] = cards[0][i]
    else:
        print("== Something strange happened. Highest =",highest)
        highest = -1
    
    cardStrengths.append(strengths)

print(cardStrengths)
    