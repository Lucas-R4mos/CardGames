class Deck:
    def __init__(self):
        self.cards = self.newDeck()

    def removeCard(self, card):
        self.cards.remove(card)
        return

    def newDeck(self):
        from cardgames.basics.card import Card
        deck = []
        suits = ["♤", "♡", "◇", "♧"]
        for suit in suits:
            for value in range(1, 14):
                newCard = Card(value, suit)
                deck.append(newCard)
        return deck

    def length(self):
        return len(self.cards)