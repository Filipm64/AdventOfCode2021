def partOne():
    f = open("puzzleInput/day1.txt", "r")
    line = int(f.readline())
    previousLine = line
    count = 0

    while line != "":

        line = int(line)

        if line > previousLine:
            count += 1

        previousLine = line
        line = f.readline()
        
    print("Count part one = ", count)

def partTwo():
    fPartTwo = open("puzzleInput/day1.txt", "r")
    line = int(fPartTwo.readline())
    line2 = int(fPartTwo.readline())
    line3 = int(fPartTwo.readline())
    line4 = int(fPartTwo.readline())
    count = 0

    while line4 != "":

        line4 = int(line4)
        sum1 = line + line2 + line3
        sum2 = line2 + line3 + line4

        if sum1 < sum2:
            count += 1

        line = line2
        line2 = line3
        line3 = line4
        line4 = fPartTwo.readline()
        
    print("Count  part two = ", count)

partOne()
partTwo()
