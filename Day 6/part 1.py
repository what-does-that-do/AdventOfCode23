file = "Day 6/test_case.txt"
f = open(file,'r')

lines = f.readlines()
t = lines[0].replace("Time:","").strip().split(' ')
d = lines[1].replace("Distance:","").strip().split(' ')

times = []
for ti in t:
    if ti.isdigit():
        times.append(ti)

distances = []
for di in d:
    if di.isdigit():
        distances.append(di)

if len(times) != len(distances):
    raise "List lengths are inequal"

multipliedPossibilities = 1
for race in range(len(times)):
    time = int(times[race])
    distance = int(distances[race])

    holdButtonFor = 0
    reachedDistance = 0
    possibilities = 0

    while holdButtonFor < time:
        timeLeft = time - holdButtonFor
        reachedDistance = timeLeft * holdButtonFor

        print(holdButtonFor,"m/s","got",reachedDistance)
        if reachedDistance >= distance:
            possibilities += 1
            print("YES")

        print("Possibilities:",possibilities)
        holdButtonFor += 1
    multipliedPossibilities *= possibilities

print(multipliedPossibilities)