file = "Day 8/input.txt"
f = open(file, 'r')
instructions = f.readlines()[0].replace('\n','')
f.close()

#currentMap = 'AAA'
#endMap = 'ZZZ'
mapp = {}

f = open(file,'r')
for line in f.readlines():
    if "=" in line:
        #print(line)
        code = line.replace('\n','').split('=')[0].strip()
        locations = line.replace('\n','').split('=')[1].replace('(','').replace(')','').split(',')
        mapp[code] = (locations[0].strip().replace('\n',''),locations[1].strip().replace('\n',''))

#print(instructions)
#print(mapp)

currentMaps = []
for m in mapp:
    if m[-1] == 'A':
        currentMaps.append(m)

print(currentMaps)

steps = 0
inst = 0
gotIt = False

while not gotIt:
    if inst < len(instructions):
        task = instructions[inst]
        steps += 1
        if task == 'R':
            for m in currentMaps:
                m2 = mapp[m][1]
                currentMaps[currentMaps.index(m)] = m2
            inst += 1
        elif task == 'L':
            for m in currentMaps:
                m2 = mapp[m][0]
                currentMaps[currentMaps.index(m)] = m2
            inst += 1
        else:
            pass
    else:
        inst = 0
    
    a = 0
    for m in currentMaps:
        if m[-1] == 'Z':
            a += 1
    if a == 2:
        gotIt = True
        print("==> DONE!")
    else:
        print(a,"maps have got a Z at the end. Iterations:",steps,end='\r')

print("currentmaps",currentMaps)
print("Steps:",steps)
