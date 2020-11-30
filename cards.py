class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.representation = f"{self.number} of {self.suit}"

    def adjustRepresentation(self):
        if self.number == 1:
            self.representation = f"A of {self.suit}"
        if self.number == 11:
            self.representation = f"J of {self.suit}"
        if self.number == 12:
            self.representation = f"Q of {self.suit}"
        if self.number == 13:
            self.representation = f"K of {self.suit}"
        return


class Deck:
    def __init__(self):
        self.cards = self.newDeck()

    def removeCard(self, card):
        self.cards.remove(card)
        return

    def pullACard(self):
        import random
        if len(self.cards) == 0:
            return Card("You have no more cards to pull.", "")
        card = random.choice(self.cards)
        self.removeCard(card)
        return card

    def newDeck(self):
        deck = []
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        for suit in suits:
            for number in range(1, 14):
                newCard = Card(number, suit)
                if newCard.number == 1 or newCard.number == 1 or newCard.number == 11 or newCard.number == 12 or newCard.number == 13:
                    newCard.adjustRepresentation()
                deck.append(newCard)
        return deck


# Para sortear uma única carta / To pick a single card
if __name__ == "__main__":
    deck = Deck()
    while True:
        card = deck.pullACard()
        print(f"Your card is a {card.representation}")
        confirmation = input("Press 'n' to quit or 'Enter' to pull a card again.")
        if confirmation == "n":
            break
        else:
            continue