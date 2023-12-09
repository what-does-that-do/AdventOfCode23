file = "Day 9/input.txt"
f = open(file,'r')

reports = []
for line in f.readlines():
    l = line.replace('\n','').split(' ')
    reports.append(l)

print("Reports =",reports)

veryTotal = 0
count = 0
for r in reports:
    print("Working hard! Current repoort =",count,"of",len(reports)," -- ",count/len(reports),"%",end='\r')
    #print("Current report =",r)
    allSame = False
    lastDiff = r
    #print("Lastdiff =",r)
    difference = 0
    differences = [[]]
    for a in r:
        differences[0].append(int(a))

    while not allSame:
        difference += 1
        lastDiff2 = []
        total = 0
        for i in range(len(lastDiff)-1):
            d = int(lastDiff[i+1])-int(lastDiff[i])
            lastDiff2.append(d)
            total += d
        lastDiff = lastDiff2
        differences.append(lastDiff2)
        #print("Difference",difference,"=",lastDiff2)
        if total == 0:
            allSame = True
            #print("Done!")
    
    #print("Differences =",differences)

    difference = len(differences)-1
    nextValue = 0
    while difference > 0:
        nextValue = differences[difference-1][-1] + differences[difference][-1]
        #print("nV=",nextValue)
        newDiffs = differences[difference-1]
        newDiffs.append(nextValue)
        differences[difference-1] = newDiffs
        #print("newDifferences =",differences)
        difference -= 1
    #print("NEXT VALUE =",nextValue)
    veryTotal += nextValue
    count += 1

print("  ==> DONE")
print("final total =",veryTotal)