from cardgames.blackjack.blackjackplayer import BlackJackPlayer


class BlackJack():
    def __init__(self):
        from cardgames.basics.deck import Deck
        self.players = list()
        self.deck = Deck()
        self.setPlayers()
        print("♤ Black ♡ ◇ Jack ♧")

    def player(self):
        return self.players[0]

    def setPlayers(self):
        player = BlackJackPlayer()
        self.players.append(player)
        return

    def getFirstPlayer(self):
        return self.players[0]

    def tryAgain(self, player):
        tryAgain = input("Try again? ('n' for no) ")
        if tryAgain == "n":
            print("See you next time.")
            exit()
        else:
            print("New game!")
        return

    def routine(self, player): # Show cards in hand/score; Decision based on score; if score < 21, +1?
        score = player.handValue()
        print(f"Hand: {player.cardList()}")
        print(f"You have {score} points.")
        if score == 21:
            print("21 ♤ BLACK ♡ 21 Congratulations! 21 ◇ JACK ♧ 21")
            self.tryAgain(player)
        elif score > 21:
            print("You lose.")
            self.tryAgain(player)
        else:
            pullDecision = input("Pull one more card? ('n' for no)")
            if pullDecision == "n":
                print(f"Your final score: {score}")
                self.tryAgain(player)
            else:
                self.oneMoreCardPlayer(player)
                self.routine(player)
        return

    def turn(self, player):
        twoCards = player.pullTwoCardsFrom(self.deck)
        print(f"Pulled two cards: {twoCards[0]} and {twoCards[1]}")
        self.routine(player)
        return

    def oneMoreCardPlayer(self, player):
        oneCard = player.pullACardFrom(self.deck)
        print(f"Pulled a card: {oneCard}")
        return

if __name__ == "__main__":
    while True:
        game = BlackJack()
        game.turn(game.player())