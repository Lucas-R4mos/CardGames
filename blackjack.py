from cardgames.blackjack.blackjackplayer import BlackJackPlayer, Dealer


class BlackJack():
    def __init__(self):
        from cardgames.basics.deck import Deck
        self.players = list()
        self.deck = Deck()
        print("♤ Black ♡ ◇ Jack ♧")

    def setPlayers(self):
        player = BlackJackPlayer()
        self.players.append(player)
        return

    def getFirstPlayer(self):
        return self.players[0]

    def playerTurn(self, player):
        twoCards = player.pullTwoCardsFrom(self.deck)
        print(f"Pulled two cards: {twoCards[0]} and {twoCards[1]}")
        print(f"You have {player.handValue()} points. Hand: {player.cardList()}")
        return player.handValue()


if __name__ == "__main__":
    game = BlackJack()
    game.setPlayers()
    game.playerTurn(game.getFirstPlayer())
