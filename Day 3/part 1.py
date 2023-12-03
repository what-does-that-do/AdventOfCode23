file = "Day 3/test_case.txt"
f = open(file,'r')

symbols = []
numbers = []
for line in f.readlines():
    lineSymbols = []
    lineNumbers = {}
    i = 0
    lastDigit = 0
    wasADigit = False

    for c in line.replace('\n',''):
        if not c.isdigit() and c != ".":
            lineSymbols.append(i)
        if c.isdigit():
            if wasADigit:
                lineNumbers[lastDigit] = lineNumbers[lastDigit] + c
            else:
                lineNumbers[i] = c
                wasADigit = True
                lastDigit = i
        else:
            wasADigit = False
        i += 1
    symbols.append(lineSymbols)
    numbers.append(lineNumbers)

print(symbols,"N",numbers)

line = 0

numberIndexes = []
for lineNos in numbers:
    indexes = []
    for n in lineNos:
        for i in range(len(lineNos[n])):
            indexes.append(n+i)
    numberIndexes.append(indexes)

print(numberIndexes)

for i in range(len(numberIndexes)):
    if i > 0:
        for n in numberIndexes[i]:
            

'''
for numbers in lineNumbers:
    indexes = []
    for index in numbers:
        if line > 0:
            indexes.append(index)
            for i in range (len(numbers[index])-1):
                indexes.append([numbers[index][i]])
'''