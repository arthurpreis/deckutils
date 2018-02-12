class DeckUtils():
    def __init__(self, gameMode = 'standard'):
        '''Use this class to set the cards values and names accordingly 
        to the games rules and language'''
        
        if gameMode == 'standard':
            self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
            self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8",
                      "9", "10", "Jack", "Queen", "King"]
                      
        elif gameMode == 'truco':
            self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
            self.ranks = ["4", "5", "6", "7", "Queen", "Jack", "King", "Ace",
                    "2", "3"]
        
        self.suitRange = len(self.suits)
        self.rankRange = len(self.ranks)
    
    def card_name(self, r, s, lang = 'en'):
        if lang == 'en':
            return self.ranks[r] + ' of ' + self.suits[s]
            
    
