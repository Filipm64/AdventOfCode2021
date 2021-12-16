def partOne():
    with open("puzzleInput/day4.txt") as f:
        drawn = [int(x) for x in f.readline().strip('\n').split(',')]
        cards = []
        while f.readline():
            card = []
            for i in range(5):
                card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
            cards.append(card)
    def isWinner(card):
        #Horizontal rows
        start = 0
        for i in range(5):
            if card[start] + card [start + 1] + card[start + 2] + card[start + 3] + card[start + 4] == 500:
                return True
            start += 5
        #Vertical columns
        start = 0
        for i in range(5):
            if card[start] + card [start + 5] + card[start + 10] + card[start + 15] + card[start + 20] == 500:
                return True
            start += 1
        #No bingos today
        return False

    found = False
    while found == False:
        number = drawn[0]
        drawn = drawn[1:]
        for card in cards:
            for i in range(len(card)):
                if card[i] == number:
                    card[i] = 100
        for card in cards:
            if isWinner(card):
                total = sum([x for x in card if x != 100])
                print("Part one solution: ", total * number)
                found = True

partOne()