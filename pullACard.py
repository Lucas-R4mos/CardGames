class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.cardRepresentation = f"{self.number} of {self.suit}"

def adjustCardRepresentation(card):
    if card.number == 1:
        card.cardRepresentation = f"A of {card.suit}"
    if card.number == 11:
        card.cardRepresentation = f"J of {card.suit}"
    if card.number == 12:
        card.cardRepresentation = f"Q of {card.suit}"
    if card.number == 13:
        card.cardRepresentation = f"K of {card.suit}"
    return

def newDeck():
    deck = []
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    for suit in suits:
        for number in range(1, 14):
            newCard = Card(number, suit)
            adjustCardRepresentation(newCard)
            deck.append(newCard)
    return deck

def pullACard(deck):
    import random
    return random.choice(deck)

# Para sortear uma única carta / To pick a single card
if __name__ == "__main__":
    deck = newDeck()
    while True:
        card = pullACard(deck)
        print(f"Your card is a {card.cardRepresentation}")
        confirmation = input("Press 'n' to quit or 'Enter' to pull a card again.")
        if confirmation == "n":
            break
        else:
            continue