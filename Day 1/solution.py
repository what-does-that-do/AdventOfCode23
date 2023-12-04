file = "Day 1/input.txt"

f = open(file, 'r')
lines = []
new_lines = []
for line in f.readlines():
    lines.append(line.replace('\n',''))

#print(lines)

def findWordSolutions(text):
    def firstAndLast(newtext):
        firstIntLocation = 100
        lastIntLocation = 0
        firstInt = 0
        lastInt = 0

        for i in range(len(newtext)): # get first and last int of that replacement.
            if newtext[i].isdigit():
                if i < firstIntLocation: # if earliest ever recorded...
                    firstIntLocation = i-1
                    firstInt = newtext[i]
                if i > lastIntLocation: # if latest ever recorded...
                    lastIntLocation = i-1
                    lastInt = newtext[i]

        return (firstInt, firstIntLocation, lastInt, lastIntLocation)
    
    firstInt, firstIntLocation, lastInt, lastIntLocation = firstAndLast(text)
    print("Initial run first and last digits are",firstInt,lastInt)
    numbers = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

    for n in numbers: # loop from 0-9
        print("TRYING N",n)
        newtext = text.replace(n,numbers[n]) # replace word to number equivalent
        print("REPLACED = ",newtext)
        firstInt2, firstIntLocation2, lastInt2, lastIntLocation2 = firstAndLast(newtext)
        print("* First int =",firstInt2," - at index =",firstIntLocation2)
        print("* Last  int =",lastInt2," - at index =",lastIntLocation2)
        if firstIntLocation2 < firstIntLocation:
            firstIntLocation = firstIntLocation2
            firstInt = firstInt2
        if lastIntLocation2 > lastIntLocation:
            lastIntLocation = lastIntLocation2
            lastInt = lastInt2
        print("After number",n,"first digit",firstInt,"last digit",lastInt)
    
    return str(firstInt) + str(lastInt)

solutions = []

for line in lines:
    print("Running findWordSolutions for line",line)
    digitSolution = findWordSolutions(line)
    print("Final digit solution for line",line,"is",digitSolution)
    solutions.append(digitSolution)

total = 0
for solution in solutions:
    total += int(solution)

print("DIGIT TOTAL =",total)
=======
f = open(file,'r')

numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
digits = []

for line in f.readlines():
    line2 = line.replace("\n","")
    print("Line =",line2)
    spelledout = ""
    firstDigit = ""
    lastDigit = ""

    for ch in line2: # slowly put together string
        if ch.isdigit():
            firstDigit = ch
            break
        else:
            spelledout = spelledout + ch

        for n in numbers: # if the string makes a number, stop and use that!
            if n in spelledout:
                firstDigit = str(numbers.index(n))
        
        if firstDigit != "":
            break
    
    spelledout = ""
    reversedLine = line2[::-1] # reverse it
    print("Reversed:",reversedLine)

    for ch in reversedLine: # go through backwards
        if ch.isdigit():
            lastDigit = ch
            break
        else:
            spelledout = spelledout + ch
        forwardSpelledout = spelledout[::-1] # flip back around
        print("FSO =",forwardSpelledout)

        for n in numbers: # if it now makes a number, stop that's the last digit!
            if n in forwardSpelledout:
                lastDigit = str(numbers.index(n))
        
        if lastDigit != "":
            break
    
    digit = firstDigit + lastDigit
    digits.append(digit)
    print("Digit =",digit)

# add it up!
total = 0
for d in digits:
    total += int(d)

print("ANSWER:",total)
