def partOne():
    f = open("puzzleInput/day3.txt", "r")
    value = f.readline()

    zeroList = []
    oneList = []

    for x in range(len(value.strip())):
        zeroList.append(0)
        oneList.append(0)

    while value != "":

        for x in range(len(zeroList)):
            bin = value[x]
            if bin == "0":
                zeroList[x] = zeroList[x] + 1
            else:
                oneList[x] = oneList[x] + 1

        value = f.readline()

    f.close()

    gammaPowerBin = ""
    epsilonBin = ""
    for x in range(len(zeroList)):
        if zeroList[x] > oneList[x]:
            gammaPowerBin += "0"
            epsilonBin += "1"
        elif zeroList[x] < oneList[x]:
            gammaPowerBin += "1"
            epsilonBin += "0"

    print("Gamma power binnary: ", gammaPowerBin)
    gammaPowerDecimal = int(gammaPowerBin, 2)
    print("Gamma power decimal: ", gammaPowerDecimal)

    print("Epsilon binary: ", epsilonBin)
    epsilonDecimal = int(epsilonBin, 2)
    print("Epsilon decimal: ", epsilonDecimal)

    print("Gamma * epsilon= ", (epsilonDecimal * gammaPowerDecimal))


def partTwo():
    print("Part two")


partOne()
