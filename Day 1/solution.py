file = "Day 1/input.txt"
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