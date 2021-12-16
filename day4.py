def partOne():
    fPartOne = open("puzzleInput/day4.txt")
    print("PartOne")
    moves = []
    moves = fPartOne.readline().split(",")
    board = []
    markedList = []

    markedList.append([False, False, False, False, False])
    markedList.append([False, False, False, False, False])
    markedList.append([False, False, False, False, False])
    markedList.append([False, False, False, False, False])
    markedList.append([False, False, False, False, False])

    for x in moves:
        print(x, end=" ")

    print("Board: ", board)

    gameContinue = True
    index = 0

    numberOfWhile = 0
    winnersInfo = []

    while gameContinue:
        numberOfWhile += + 1
        print("While is running ", numberOfWhile, " times")

        board.clear()
        fPartOne.readline()
        board.append(fPartOne.readline().replace("  ", " ").strip().split(" "))
        board.append(fPartOne.readline().replace("  ", " ").strip().split(" "))
        board.append(fPartOne.readline().replace("  ", " ").strip().split(" "))
        board.append(fPartOne.readline().replace("  ", " ").strip().split(" "))
        board.append(fPartOne.readline().replace("  ", " ").strip().split(" "))

        markedList.clear()
        markedList.append([False, False, False, False, False])
        markedList.append([False, False, False, False, False])
        markedList.append([False, False, False, False, False])
        markedList.append([False, False, False, False, False])
        markedList.append([False, False, False, False, False])

        numberOfMoves = 0

        for x in moves:
            numberOfMoves += + 1
            for i in range(5):
                for y in range(5):
                    if board[i][y] == x:
                        markedList[i][y] = True
                        for w in range(5):
                            if markedList[w][0] & markedList[w][1] & markedList[w][2] & markedList[w][3] & markedList[w][4] | markedList[0][w] & markedList[1][w] & markedList[2][w] & markedList[3][w] & markedList[4][w]:
                                 # winnerInfo = [numberOfMoves, lastMove, unmarkedCount]
                                
                                 unmarkedCount = 0
                                 lastMove = int(x)

                                 for n in range(5):
                                    for o in range(5):
                                        if markedList[n][o] == False:
                                            unmarkedCount += + int(board[n][o])
                                 winnersInfo.append([numberOfMoves, lastMove, unmarkedCount])

                                
                                 
        index += + 1
        if index >= len(moves):
            gameContinue = False

    finalWinner = winnersInfo[0][0]
    print("Winnerinfo00 ", winnersInfo[0][0])
    for n in winnersInfo:
        print("n ", n[0])
        print("Final winner ",finalWinner)
        if n[0] < finalWinner:
            finalWinner = n
    print("Final winner: ", finalWinner[0])
    score = int(finalWinner[1]) * int(finalWinner[2])
    print("Final score: ", score)
    
    fPartOne.close()

    
    

    
    

partOne()