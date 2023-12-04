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
    i2 = []
    for n in lineNos:
        for i in range(len(lineNos[n])):
            indexes.append(n+i)
        indexes.append(i2)
    numberIndexes.append(indexes)

print(numberIndexes)
partNumbers = []

for line in range(len(numberIndexes)):
    for fullNumber in numberIndexes[line]:
        if not str(fullNumber).isdigit():
            continue
        
        print("line=",line)
        if line == 0:
            start = line-1
        else:
            start = 0
        
        if line+1 >= len(numberIndexes)-1:
            end = len(numberIndexes)
        else:
            end = line+1
        
        for l in range(start,end+1):
            print("l=",l,"start=",start,"end=",end)
            working = False
            print("fullNumber",fullNumber)
            for num in str(fullNumber):
                print(fullNumber)
                n = int(num)
                if n in symbols[l]:
                    print(n,"is in symbols.")
                    working = True
                elif n+1 in symbols[l]:
                    print(n,"is next along in symbols!")
                    working = True
                elif n-1 in symbols[l]:
                    print(n,"is one behind in symbols.")
                    working = True
                if working:
                    partNumbers.append(fullNumber)
                    break
                
print(partNumbers)
            

'''
for numbers in lineNumbers:
    indexes = []
    for index in numbers:
        if line > 0:
            indexes.append(index)
            for i in range (len(numbers[index])-1):
                indexes.append([numbers[index][i]])
'''