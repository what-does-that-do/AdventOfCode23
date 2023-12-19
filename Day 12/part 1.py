file = "Day 12/test_case.txt"
f = open(file,'r')

for line in f.readlines():
    formatted = line.replace('\n','').strip()
    conditions = formatted.split(' ')[0]
    noConditions = formatted.split(' ')[1].split(',')
    
    posGroups = []
    pos = 0
    for spring in conditions:
        if spring == '#' or spring == '?':
            pos += 1
        else:
            if pos != 0:
                posGroups.append(pos)
            pos = 0
    if pos != 0:
        posGroups.append(pos)

    print(posGroups)

    for condition in noConditions:
        for g in range(len(posGroups)):
            if int(condition) == g:
                posGroups[g] = posGroups[g] - int(condition)
            elif int(condition) > g:
                posGroups[g] = posGroups[g] - int(condition)+1
    
    print("n",posGroups)
            