# deckutils
Playing card and stack of cards objects and basic functions in python.

## Card

    c = Card(s, r)

To create a card object of suit 's' and rank 'r'. 
To get a string with the card's name (in english):

    cardName = str(c) 
    
Check deckutils.py to change the names of the cards.    

Comparisons operators (``` >, <, <=, >=, ==, !=```) between cards use rank
and suit values (in this order) to evaluate them.

## Stack

    s = Stack()

Ordered collection of cards (contained in a list). 

* To add 'c' card to a stack 's' you can:

1. use the add operator '+':

    s = s + c
    s += c
    
2. use the '.append()' function:

    s.append(c)

3. You can also add the cards from another 't' stack:

    s = s + t
    s += t

* To remove a card from your stack:

1. use '.remove(n)' to remove the n-th card or or '.remove(c)' to 
remove a card with the same values as c

    s.remove(n)
    s.remove(c)

2. use the minus operator '-' to remove a card with the same value as 'c'

    s = s - c
    s -= c
   
if there's no such card in the stack, nothing happens

3. use the minus operator '-' to remove cards that two stacks have in common

    s = s - t
    s -= t
    
if there aren't such cards in the stack, nothing happens

4. to remove *all* cards from your stack:
    s.empty()

* To get a card from your stack:

1. use the index to return the n-th card from your stack:
    
    c = s[n]
    
2. use the '.pop(n)' funcion to return the n-th card from your stack or 
'.pop(d)' to return card with the same value as 'd'. In both cases, the card is removed from the stack

    c = s.pop(n)
    c = s.pop(d)

* To move cards between stacks:
1. '.move()' to remove the n-th card or to remove a card
with the same value as 'c' and add it to 't':

    s.move(n, t)
    s.move(c, t)
    
* To shuffle a stack:

    s.shuffle()
    
* To order a stack
1. ordering by rank then by suit:
    s.order()
    s.order('rank')
    
2. ordering by suit then by rank:
    s.order('suit')
    
* Comparing and check stacks:

1. To check if two stacks are identical (contains the same cards and in the same order):
    s == t

2. To check if a card with the same values as 'c' belongs to stack:
    c in s

3. the number of cards in a stack is:
    n = len(s)
    
4. you can also check if a stack is empty with:
    s.is_empty()
    
## Deck

    dk = Deck()

A deck is a special kind of stack which is created containing one card
of each combination of suits and ranks.
