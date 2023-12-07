file = "Day 5/input.txt"
f = open(file,'r')

maps = {}
inp = []
current = ""
for line in f.readlines():
    l2 = line.replace('\n','')
    if ':' in l2:
        current = l2.split(':')[0].replace('map','').strip()
        if current == "seeds":
            inp = l2.split(':')[1].split(' ')
        else:
            maps[current] = []
    elif l2 == "":
        continue
    else:
        print(current)
        if current != "seeds":
            m = maps[current]
            m.append(l2.split(' '))
            maps[current] = m

soil = []
for s in inp:
    newSeed = s
    for m in maps['seed-to-soil']:
        if s < int(m[1]) < int(m[1]) + int(m[2]): # if inside source range
            toDo = int(m[0]) - int(m[1])
            newSeed = s + toDo

print("Seeds =",inp)
print("Maps =",maps)
print("New seed",newSeed)