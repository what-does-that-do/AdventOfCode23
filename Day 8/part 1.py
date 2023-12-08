file = "Day 8/input.txt"
f = open(file, 'r')
instructions = f.readlines()[0].replace('\n','')
f.close()

currentMap = 'AAA'
endMap = 'ZZZ'
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

steps = 0
inst = 0

print(currentMap,endMap)
while currentMap != endMap:
    if inst < len(instructions):
        task = instructions[inst]
        steps += 1
        if task == 'R':
            currentMap = mapp[currentMap][1]
            print(currentMap,'R',mapp[currentMap])
            inst += 1
        elif task == 'L':
            currentMap = mapp[currentMap][0]
            print(currentMap,'L',mapp[currentMap])
            inst += 1
        else:
            pass
    else:
        inst = 0
    #print(currentMap," - steps -",steps,end='\r')

print("currentmap",currentMap)
print("Steps:",steps)