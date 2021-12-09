f = open("day1.txt", "r")

line = int(f.readline())
previousLine = line
count = 0

while line != "":

    line = int(line)

    if line > previousLine:
        count = count + 1

    previousLine = line
    line = f.readline()
    
print("Count = ", count)
