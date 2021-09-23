import random


class deck():
    def __init__(self):
        # Stop point is when the casino will stop, usually when 60 - 75 cards are left
        self.stopPoint = random.randint(60, 75)
        self.numDecks = 6  # Set to 6, the most common variant in the casino

        # J, Q, K are all counted as 10 points
        cardStr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        deckArr = []
        for x in range(self.numDecks):
            for i in range(4):
                for j in range(13):
                    deckArr.append(cardStr[j])

        self.deckArr = deckArr

    def shuffle(self):
        random.shuffle(self.deckArr)

    def deal(self):
        return self.deckArr.pop()  # Deals the card

    def endReached(self):  # Checks if the stop point should be reached
        if len(self.deckArr) < self.stopPoint:
            return True
        return False
