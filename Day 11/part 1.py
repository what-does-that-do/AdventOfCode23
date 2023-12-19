file = "Day 11/test_case.txt"

galaxyMap = []

def showMap(galaxyMap):
    for m in galaxyMap:
        print(m)

with open(file,'r') as f:
    for line in f.readlines():
        galaxyMap.append(line.replace('\n','').strip())

print("GALAXY MAP:")
showMap(galaxyMap)

newGalaxyMap = []

# Find empty rows
for g in range(len(galaxyMap)):
    galaxies = 0
    for c in galaxyMap[g]:
        if c == '#':
            galaxies += 1
    if galaxies == 0:
        newLine = ""
        for i in range(len(galaxyMap[g])):
            newLine += '.'
        newGalaxyMap.append(newLine)
    newGalaxyMap.append(galaxyMap[g])

galaxyMap = newGalaxyMap
print("ROWS GALAXY MAP:")
showMap(galaxyMap)

newGalaxyMap = []

for g in range(len(galaxyMap[0])):
    galaxies = 0
    for c in range(len(galaxyMap)):
        if galaxyMap[c][g] == '#':
            galaxies += 1
    if galaxies == 0:
        newLine = ""
        rep = 2
    else:
        rep = 1s
    for r in range(rep):
        for i in range(len(galaxyMap)):
            if len(newGalaxyMap) == i:
                newGalaxyMap.append('')
            newGalaxyMap[i] = newGalaxyMap[i] + galaxyMap[i][g]

galaxyMap = newGalaxyMap
print("COLS GALAXY MAP:")
showMap(galaxyMap)

# Find distances
