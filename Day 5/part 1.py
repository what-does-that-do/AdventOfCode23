file = "Day 5/input.txt"
f = open(file,'r')

maps = {}
inp = []
current = ""
for line in f.readlines():
    if ':' in line:
        current = line.split(':')[0].replace('map','').strip()
        if current == "seeds":
            inp = line.split(':')[0].split(' ')
        else:
            maps[current] = []
    elif line == "":
        continue
    else:
        print(current)
        if current != "seeds":
            print(line.split(' '))
            maps[current] = maps[current].append(line.split(' '))

print("Seeds =",inp)
print("Maps =",maps)