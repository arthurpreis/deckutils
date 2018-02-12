from card import Card
from stack import Stack
from deckutils import DeckUtils

dk = DeckUtils()

class Deck(Stack):
    def __init__(self):
        self.new_deck()

    def new_deck(self):
        self.cards = []
        for suit in range(dk.suitRange):
            for rank in range(dk.rankRange):
                self.cards.append(Card(suit,rank))

if __name__ == '__main__':
    d = Deck()
    print(d)
