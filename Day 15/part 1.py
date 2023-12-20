f = open("Day 15/input.txt", "r")

def hash_algorithm(stringIn):
    current = 0
    for c in stringIn:
        current += ord(c) # increase current by ASCII code
        current *= 17
        current = current % 256
    return current

for line in f.readlines():
    l = line.replace("\n", "")
    sequences = l.split(",")

    currentTotal = 0
    for s in sequences:
        current = hash_algorithm(s)
        print(s,"becomes",current)
        currentTotal += current
    print()

print("ANSWER:")
print(currentTotal) 