class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.representation = self.defineRepresentation()

    def defineRepresentation(self):
        if self.value == 1:
            return "A"
        elif self.value == 11:
            return "J"
        elif self.value == 12:
            return "Q"
        elif self.value == 13:
            return "K"
        else:
            return str(self.value)
        return

class Deck:
    def __init__(self):
        self.cards = self.newDeck()

    def removeCard(self, card):
        self.cards.remove(card)
        return

    def pullACard(self):
        import random
        card = random.choice(self.cards)
        self.removeCard(card)
        return card

    def newDeck(self):
        deck = []
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        for suit in suits:
            for value in range(1, 14):
                newCard = Card(value, suit)
                deck.append(newCard)
        return deck

    def length(self):
        return len(self.cards)

# Para sortear uma única carta / To pick a single card
if __name__ == "__main__":
    deck = Deck()
    while True:
        card = deck.pullACard()
        print(f"Your card is a {card.representation} of {card.suit}")
        if deck.length() == 0:
            confirmation = input("You have no more cards to pull. Press Enter to start a new deck or 'n' to exit.")
            if confirmation == "n":
                break
            else:
                deck = Deck()
        else:
            confirmation = input(f"Press 'n' to quit or 'Enter' to pull a card again. {deck.length()} cards remaining.")
            if confirmation == "n":
                break
            else:
                continue