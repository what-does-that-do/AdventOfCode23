file = "Day 7/input.txt"
f = open(file,'r')

cards = [[],[]] # [type], [bid]
ranks = {}
rankOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
kinds = ["Five of a kind","Four of a kind","Full house","Three of a kind","Two pair","One pair","High card"]
cardChars = []

for line in f.readlines():
    l = line.replace('\n','').split(" ")
    cards[0].append(l[0])
    cards[1].append(l[1])
    cc = {}
    for r in rankOrder:
        cc[r] = l[0].count(r)
    cardChars.append(cc)

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
            if "One pair" in strengths:
                s = strengths['One pair'] 
                s.append(cards[0][i])
                strengths['One pair'] = s
            else:
                strengths['One pair'] = [cards[0][i]]
        else:
            if "Two pair" in strengths:
                s = strengths['Two pair'] 
                s.append(cards[0][i])
                strengths['Two pair'] = s
            else:
                strengths['Two pair'] = [cards[0][i]]
    elif highest == 3:
        two = False
        for c in chars:
            if int(chars[c]) == 2:
                two = True
        if two:
            if "Full house" in strengths:
                s = strengths['Full house'] 
                s.append(cards[0][i])
                strengths['Full house'] = s
            else:
                strengths['Full house'] = [cards[0][i]]
        else:
            if "Three of a kind" in strengths:
                s = strengths['Three of a kind'] 
                s.append(cards[0][i])
                strengths['Three of a kind'] = s
            else:
                strengths['Three of a kind'] = [cards[0][i]]
    elif highest == 4:
        if "Four of a kind" in strengths:
            s = strengths['Four of a kind'] 
            s.append(cards[0][i])
            strengths['Four of a kind'] = s
        else:
            strengths['Four of a kind'] = [cards[0][i]]
    elif highest == 5:
        if "Five of a kind" in strengths:
            s = strengths['Five of a kind'] 
            s.append(cards[0][i])
            strengths['Five of a kind'] = s
        else:
            strengths['Five of a kind'] = [cards[0][i]]
    else:
        #print("== Something strange happened. Highest =",highest)
        highest = -1
    
    #cardStrengths.append(strengths)


#BUBBLE SORT
newCardList = []
for kind in kinds:
    if kind in strengths:
        print("Checking",kind,"in",strengths[kind])
        kindList = []
        changes = 0
        while changes > 0:
            if len(strengths[kind]) > 1:
                for i in range(1,len(strengths[kind]),2):
                    print("Checking",strengths[kind][i])
                    for j in range(len(strengths[kind][i])):
                        print("Comparing",strengths[kind][i-1][j],"with",strengths[kind][i][j])
                        if rankOrder.index(strengths[kind][i-1][j]) > rankOrder.index(strengths[kind][i][j]):
                            print(strengths[kind][i][j],"is a higher rank than",strengths[kind][i-1][j])
                            
                            kindList.insert(0, strengths[kind][i])
                            kindList.insert(0, strengths[kind][i-1])
                            print("Added",strengths[kind][i],"after",strengths[kind][i-1])
                            break
                        elif rankOrder.index(strengths[kind][i-1][j]) < rankOrder.index(strengths[kind][i][j]):
                            print(strengths[kind][i-1][j],"is a higher rank than",strengths[kind][i][j])
                            
                            kindList.insert(0, strengths[kind][i-1])
                            kindList.insert(0, strengths[kind][i])
                            print("Added",strengths[kind][i-1],"after",strengths[kind][i])
                            break
            else:
                print("Only one occurence of",strengths[kind],"adding to list.")
                newCardList.insert(0, strengths[kind][0])
        newCardList = newCardList + kindList
print(strengths)
print(newCardList)

total = 0
for c in newCardList:
    bid = cards[1][cards[0].index(c)]
    rank = newCardList.index(c)+1
    #print("Bid of",c,"=",bid)
    #print("Rank of",c,"=",rank)
    winnings = int(bid) * int(rank)
    total += winnings
print("TOTAL =",total)