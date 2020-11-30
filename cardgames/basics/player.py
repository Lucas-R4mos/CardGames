class Player:
    def __init__(self):
        self.hand = list()
        self.name = None
    
    def pullACardFrom(self, deck):
        import random
        from cardgames.basics.card import Card
        card = random.choice(deck.cards)
        self.hand.append(card)
        deck.removeCard(card)
        return card.representation

    def setName(self):
        self.name = input("Insert player name: ")
        return