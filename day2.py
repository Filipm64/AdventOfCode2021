def partOne():
    forward = 0
    depth = 0

    f = open("puzzleInput/day2.txt", "r")
    value = f.readline()

    while value != "":
        
        values = value.split()
        
        if values[0] == "forward":
            forward = forward + int(values[1])
        elif values[0] == "up":
            depth = depth - int(values[1])
        elif values[0] == "down":
            depth = depth + int(values[1])

        values.clear()
        value = f.readline()
    
    result = forward * depth
    print("Part one result: ", result)

def partTwo():
    forward = 0
    depth = 0
    aim = 0

    fPartTwo = open("puzzleInput/day2.txt", "r")
    value = fPartTwo.readline()

    while value != "":
        
        values = value.split()
        
        if values[0] == "forward":
            forward += int(values[1])
            depth += int(values[1]) * aim
        elif values[0] == "up":
            aim -= int(values[1])
        elif values[0] == "down":
            aim += int(values[1])

        values.clear()
        value = fPartTwo.readline()
    
    result = forward * depth
    print("Part two result: ", result)


partOne()
partTwo()