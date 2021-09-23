class player():
    def __init__(self, money):
        self.money = money
        self.bet = 0
        self.score = 0
        self.hand = []
        self.wins = 0
        self.losses = 0
        self.winRatio = 0

    def draw(self, card):
        self.hand.append(card)
        self.setScore()

    def setScore(self):
        tmpScore = 0

        for card in self.hand:
            tmpScore += card

        if 1 in self.hand and tmpScore <= 11:  # If ace can be used as 11
            tmpScore += 10

        self.score = tmpScore

    def setWinRatio(self):
        self.winRatio = self.wins/(self.wins + self.losses)

    def isBlackjack(self):
        if len(self.hand) == 2 and self.score == 21:
            return True
        return False

    def fold(self):
        self.hand = []
        self.money -= self.bet / 2

    def win(self, bj=False):
        self.wins += 1
        if bj:
            self.money += self.bet * (3/2)
        else:
            self.money += self.bet

        self.bet = 0

    def lose(self):
        self.losses += 1
        self.money -= self.bet

        self.bet = 0
