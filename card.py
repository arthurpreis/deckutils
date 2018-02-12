from deckutils import DeckUtils

dk = DeckUtils("standard")

class Card():
    def __init__(self, suit=0, rank=0):
        '''Creates a Card object. Check deckutils.py to set ranks and 
        faces according to your game'''
        if (suit >= dk.suitRange) or (suit < 0):
            raise ValueError("Suit value {0} was requested, but deck has only {1} suit range".format(suit, dk.suitRange))

            return
        if (rank >= dk.rankRange) or (rank < 0):
            raise ValueError("Rank value {0} was requested, but deck has only {1} rank range.".format(suit, dk.rankRange))
            return
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Returns string with cards name (in english).
        Edit deckutils for additional languages support'''
        return dk.card_name(self.rank, self.suit, 'en')
        
    #comparisons    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return (self.rank < other.rank)

    def __le__(self, other):
        if self.rank == other.rank:
            return self.suit <= other.suit
        else:
            return(self.rank <= other.rank)

    def __gt__(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        else:
            return(self.rank > other.rank)

    def __ge__(self, other):
        if self.rank == other.rank:
            return self.suit >= other.suit
        else:
            return(self.rank >= other.rank)

    def __eq__(self, other):
        if isinstance(other, Card):
            return ((self.rank == other.rank) and (self.suit == other.suit))
        else:
            raise TypeError("card.__eq__() accepts only cards as arguments.")
            
    def __ne__(self,other):
        return not(self.__eq__(other))
        
