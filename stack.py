from card import Card
import random

class Stack():
    def __init__(self, cards = []):
        '''stack contains a list of cards'''
        self.cards = []
        for c in cards:
            self.cards.append(c)

    def __len__(self):
        return len(self.cards)
        
    def __add__(self, other):
        '''adds a card or another stack to a stack'''
        if isinstance(other, Stack):
            s = Stack()
            s.cards = self.cards + other.cards
            return s
        elif isinstance(other, Card):
            s = Stack()
            s.cards = self.cards[:]
            s.append(other)
            return s
        elif isinstance(other, list):
            s = Stack()
            s.cards = self.cards[:]
            s.cards += other
            return s
        else:
            raise TypeError("stack.__add__() accepts only cards and stacks as arguments.")
            return None
                      
    def __sub__(self, other):
        '''subtracts a card or stack of card from a stack.
        If there's no such cards in the stack, does nothing.'''
        if isinstance(other, Stack):
            s = Stack()
            s.cards = self.cards[:]
            for c in other.cards:
                try:
                    s.remove(c)
                except ValueError:
                    return None
            return s
        elif isinstance(other, Card):
            s = Stack()
            s.cards = self.cards[:]
            try:
                s.remove(other)
            except ValueError:
                return None
            return s
        elif isinstance(other, list):
            self.cards.append(other)
            return self
        else:
            raise TypeError("stack.__sub__() accepts only cards and stacks as arguments.")
            return None
    
    def __getitem__(self, index):
        '''returns a the i-eth card object from the stack'''
        if index > len(self):
            raise IndexError("stack.__getitem__() error:{0}-th card requested, but this stack only have {1} card(s)".format(index+1, len(self)))
            return
        else:
            return self.cards[index]
        
    def __eq__(self, other):
        '''Returns true if the cards in a stack are equal to the *respective* cards in another stack.'''
        
        if isinstance(other, Stack):
            return self.cards[:] == other.cards[:]
        else:
            raise TypeError("stack.__eq__() accepts only stacks as arguments.")
            return

    def order(self, mode = 'rank'):
        '''orders cards'''
        if (mode == 'rank'):
            self.cards = sorted(self.cards, key=lambda card: (card.rank, card.suit))
        elif (mode == 'suit'):
            self.cards = sorted(self.cards, key=lambda card: (card.suit, card.rank))        

    def __contains__(self, other):
        '''returns true if there's a card object with the same rank and suit value in stack'''
        return other in self.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        if self.is_empty():
            return 'is empty'
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s

    def append(self, other):
        if isinstance(other, Card):
            self.cards.append(other)
        else:
            raise TypeError("stack.append() accepts only cards as arguments")
            
    def remove(self, c):
        '''remove the c-eth card in a stack or removes from the stack a 
        card with the same values as the one passed as arg.'''
        if isinstance(c, Card):
            self.cards.remove(c)
        elif isinstance(c, int):
            del self.cards[c]
        else:
            raise TypeError("stack.remove() accepts only cards and integers as arguments.")
            
    def pop(self, c):
        '''returns the c-eth card in a stack or returns a card with the 
        same values as the one passed as arg. The card is then removed from
        the stack'''
        if isinstance(c, Card):
            for i in range(len(self)):
                if c == self.cards[i]:
                    return self.cards.pop(i)
            raise IndexError("Card r={0} s={1} not found in stack".format(c.rank, c.suit))
        if isinstance(c, int):
            return self.cards.pop(c)
            
    def move(self, c, t):
        '''removes the c-eth card in a stack and add it to another stack or removes
        a card with the same values as the one passed as arg then adds it to 
        another stack'''
        if isinstance(c, Card):
            t.append(self.pop(c))
            
        if isinstance(c, int):
            if c > len(self):
                raise IndexError("stack.move(): error: {0}-th card requested, but this stack only have {1} card(s)".format(index+1, len(self)))
            else:
                t.append(self.pop(c))
 
    def empty(self):
        self.cards = []
        
    def is_empty(self):
        return len(self) == 0
