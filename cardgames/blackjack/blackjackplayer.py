from cardgames.basics.player import Player

class BlackJackPlayer(Player):
    def __init__(self):
        super().__init__()

    def handValue(self):
        value = 0
        if len(self.hand) == 0:
            return 0
        for card in self.hand:
            if card.value == 11 or card.value == 12 or card.value == 13:
                value += 10
            else:
                value += card.value
        if len(self.hand) == 2 and (self.hand[0].value == 1 or self.hand[1].value == 1) and value == 11: # BlackJack!
            value = 21
        return value

    def pullTwoCardsFrom(self, deck):
        card1 = self.pullACardFrom(deck)
        card2 = self.pullACardFrom(deck)
        return [card1, card2]

    def cardList(self):
        cardList = ""
        for card in self.hand:
            cardList += card.representation + " "
        if cardList == "":
            return "Empty hand."
        return cardList