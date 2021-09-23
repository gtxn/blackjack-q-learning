from deck import deck
from player import player


class environment():
    def __init__(self):
        self.deck = deck()
        self.player = player(500)
        self.casino = player(10000000)  # Money of casino doesn't matter
        self.minBet = 10

        # Casino's first card, player score, running card count, cards drawn out of the deck
        self.state = [-1, -1, 0, 0]

        # Environment's parameterisation
        arr = []
        param = 0
        for pScore in range(2, 22):
            for cCard in range(1, 11):
                for possibleCount in range(-30, 30):
                    for cardsDrawn in range(4, 312):
                        arr.append([cCard, pScore, possibleCount, cardsDrawn])
        self.states = arr
        self.numStates = len(arr)
        self.actions = (0, 1)

        self.deck.shuffle()

    def firstDeal(self):
        self.player.hand = []
        self.casino.hand = []
        for i in range(2):
            self.player.draw(self.deck.deal())
            self.casino.draw(self.deck.deal())

        # Setting state
        self.state[0] = self.casino.hand[0]
        self.state[1] = self.player.score

        # Keeping a simple running count
        for x in self.player.hand:
            self.updateCount(x)
        self.updateCount(self.casino.hand[0])

        # Counting number of cards drawn
        self.state[3] += 4

    def step(self, action):
        print('step action', action)
        # 0 means draw , 1 means stand
        initState = self.state
        c = 0

        playerDone = False
        if self.player.score > 21:
            playerDone = True

        elif action == 0:
            c = self.deck.deal()
            self.player.draw(c)

            self.updateCount(c)
            self.state[3] += 1  # Update number of cards left in the deck

        elif action == 1:
            playerDone = True

        print('card drawn: ', c)

        if self.player.score <= 21:
            # Update state only if it's less than 21
            self.state[1] = self.player.score

        reward = self.reward(self.state, playerDone)
        return self.state, reward, playerDone

    def reward(self, state, playerDone):
        if not playerDone:  # If player is not done it is impossible to count reward
            return 0

        while self.casino.score <= 16:
            self.casino.draw(self.deck.deal())

        print('Casino score: ', self.casino.score)
        if self.isPlayerWin():
            return 1
        return -1

    def status(self):
        print('player: ', self.player.hand, self.player.score)
        print('casino: ', self.casino.hand, self.casino.score)
        print('player wins: ', self.player.wins,
              '| player losses: ', self.player.losses,
              '| win ratio: ', self.player.winRatio)
        print('state: ', self.state)
        print('-----------------------------------')

    def isPlayerWin(self):
        if self.casino.score > 21 and self.player.score > 21:  # If both bust, casino wins
            return False
        elif self.player.score > 21:
            return False
        elif self.casino.score > 21:
            return True
        elif self.casino.score >= self.player.score:
            return False
        else:
            return True

    def reset(self):
        if self.deck.endReached():
            self.deck = deck()
            self.deck.shuffle()
            self.firstDeal()
            return self.state
        self.player.hand = []
        self.casino.hand = []
        self.state = [-1, -1, 0, 0]
        self.firstDeal()
        return self.state

    def updateCount(self, card):
        if card >= 10 or card == 1:
            self.state[2] -= 1
        elif card <= 6 and card != 1:
            self.state[2] += 1

    def parameterise(self, stateToParam):
        return self.states.index(stateToParam)
