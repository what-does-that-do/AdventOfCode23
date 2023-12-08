file = "test_case.txt"
f = open(file, 'r')
instructions = f.readlines()[0]
f.close()
mapp = {}

f = open(file,'r')
for line in f.readlines():
    if "=" in line:
        print(line)
        code = line.replace('\n','').split('=')[0].strip()
        locations = line.replace('\n','').split('=')[1].replace('(','').replace(')','').split(',')
        mapp[code] = (locations[0].strip(),locations[1].strip())

print(instructions)
print(mapp)

steps = 0
currentMap = 'AAA'
for task in instructions:
    steps += 1
    if task == 'R':
        currentMap = mapp[currentMap][1]
    else:
        currentMap = mapp[currentMap][0]

print("currentmap",currentMap)
print(steps)