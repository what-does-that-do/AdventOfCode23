f = open("Day 15/input.txt", "r")
boxes = []

for i in range(256):
    boxes.append({})

def hash_algorithm(stringIn):
    current = 0
    for c in stringIn:
        current += ord(c) # increase current by ASCII code
        current *= 17
        current = current % 256
    return current

print("FILLING BOXES...")
for line in f.readlines():
    l = line.replace("\n", "")
    sequences = l.split(",")
    for s in sequences:
        #print("SEQUENCE:", s)
        if "=" in s:
            boxId = hash_algorithm(s.split("=")[0])
        else:
            boxId = hash_algorithm(s.split("-")[0])
        #print(s.split("=")[0],"=",boxId)
        box = boxes[boxId]
        if '=' in s:
            #print("Adding", s.split("=")[0],"to box", boxId)
            box[s.split("=")[0]] = s.split("=")[1]
        else:
            #print("Removing", s.split("-")[0],"from box", boxId)
            box.pop(s.split("-")[0], None)
        boxes[boxId] = box

print("CALCULATING TOTAL...")
id = 1
total = 0
for box in boxes:
    s = 1
    for slot in box:
        total += id * s * int(box[slot])
        s += 1
    id += 1

print("TOTAL =",total)