import unittest
from card import Card
from deckutils import DeckUtils

dk = DeckUtils('standard')

class TestCard(unittest.TestCase):
    
    def test_rank(self):
        c1 = Card(0, 0)
        c2 = Card(1, 1)
        c3 = Card(2,9)
                        
        self.assertEqual(c1.rank, 0)
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c3.rank, 9)
        
    def test_suit(self):
        c1 = Card(0, 0)
        c2 = Card(1, 1)
        c3 = Card(2, 9)
                        
        self.assertEqual(c1.suit, 0)
        self.assertEqual(c2.suit, 1)
        self.assertEqual(c3.suit, 2)
    
    def test_init(self):
        self.assertRaises(ValueError, Card, dk.suitRange + 1, 0)
        self.assertRaises(ValueError, Card, -1, 0)
        
        self.assertRaises(ValueError, Card, 0, dk.rankRange + 1)
        self.assertRaises(ValueError, Card, 0, -1)
            
    def test_print(self):
        c1 = Card(0, 0)
        c2 = Card(1, 1)
        c3 = Card(2, 9)
        
        self.assertEqual(str(c1), "Ace of Clubs")
        self.assertEqual(str(c2), "2 of Diamonds")
        self.assertEqual(str(c3), "10 of Hearts")
        
    def test_compare(self):
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 9)
        
        c4 = Card(1, 0)
        c5 = Card(1, 1)
        c6 = Card(1, 9)
        
        c7 = Card(3, 0)
        c8 = Card(3, 1)
        c9 = Card(3, 9)
        c10 = Card(0,0)
        
        self.assertTrue( c1 < c2)
        self.assertTrue( c2 < c3)
        self.assertTrue( c4 > c1)
        self.assertTrue( c3 > c4)
        self.assertTrue( c5 > c7)
        self.assertTrue( c1 == c10)
        self.assertTrue( c1 != c2)

if __name__=='__main__':
    unittest.main()
