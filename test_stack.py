import unittest
from card import Card
from stack import Stack

class TestCard(unittest.TestCase):
    
    def test_len_add(self):
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        s4 = Stack()
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        
        self.assertEqual(len(s1), 0)
        
        s1 = s1 + c1
        
        self.assertTrue(isinstance(s1, Stack))
        self.assertEqual(len(s1), 1)
        
        s1 = s1 + c2 + c3
        self.assertEqual(len(s1), 3)
        
        s2 += s1
        self.assertEqual(len(s2), 3)

        s2 += c1
        self.assertEqual(len(s2), 4)
        
        s2 = s1 + s2 + c3
        s2 = s1 + s2 + c3
        s2 = s1.__add__(c3)
        self.assertTrue(isinstance(s1, Stack))
        self.assertTrue(isinstance(c3, Card))
        self.assertEqual(len(s1), 3)
        
        self.assertRaises(TypeError, Stack, s1, 1)
        
        # s3 = c1 + c2
        # self.assertTrue(isinstance(s3, Stack))
        # self.assertEqual(len(s3), 2)
        #print(type(c1 + c2))
        s4 = Stack((c1, c2 , c3))
        # self.assertTrue(isinstance(s3, Stack))
        # self.assertEqual(len(s4), 3)
        
    def test_compare(self):
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)    
        
        s1 = s1 + c1 + c2 + c3
        s2 = s2 + c1 + c2 + c3
        s3 = s3 + c2 + c3 + c1
        
        self.assertTrue(s1 == s2)
        self.assertFalse(s1 == s3)
        
    def test_index(self):
        s1 = Stack()
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        
        s1 = s1 + c1 + c2 + c3
        
        self.assertEqual(s1[0], c1)
        self.assertEqual(s1[1], c2)
        self.assertEqual(s1[-1], c3)
        
        with self.assertRaises(IndexError):
            s1[5]
        
    def test_order(self):
        s1 = Stack()
        s2 = Stack()
        
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        
        s1 = s1 + c1 + c2 + c3
        s2 = s2 + c3 + c2 + c1
        
        self.assertNotEqual(s1, s2)
        s2.order()
        
        self.assertEqual(s1, s2)
        
        c4 = Card(1, 0)
        c5 = Card(1, 1)
        
        s3 = Stack()
        s4 = Stack()
        
        s3 = s3 + c1 + c4 + c5
        s4 = s4 + c4 + c1 + c5
        
        self.assertNotEqual(s3, s4)
        s4.order()
        
        self.assertTrue(s3.__eq__(s4))
        
    def test_contain(self):
        s1 = Stack()
        c1 = Card(0,0)
        c2 = Card(0,1)
        c3 = Card(0,2)
        c4 = Card(0,0)
        
        self.assertFalse(c1 in s1)
        
        s1 = s1 + c1 + c2 + c3
        
        self.assertTrue(c2 in s1)
        self.assertTrue(c4 in s1)
        
    def test_remove(self):
        s1 = Stack()
        c1 = Card(0,0)
        c2 = Card(0,1)
        c3 = Card(0,2)
        c4 = Card(0,3)
        
        s1 = s1 + c1 + c2 + c3 + c4
        self.assertTrue(c3 in s1)
        
        s1.remove(0)
        s1.remove(c3)
        self.assertFalse(c3 in s1)
        self.assertFalse(c1 in s1)
    
    def test_sub(self):
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        c4 = Card(0, 3)
        
        s3 += c1
        s3 += c2
                
        s1 = s1 + c1 + c2 + c3
        s2.cards = s1.cards[:]
        
        s1 = s1 - c1
        s1 = s1 - c4
        self.assertFalse(c1 in s1)
        self.assertEqual(len(s1), 2)
        self.assertFalse(c4 in s1)
        
        self.assertEqual(len(s2), 3)
        self.assertEqual(len(s3), 2)
        s2 = s2.__sub__(s3)
        
        self.assertTrue(isinstance(s3, Stack))
        
        self.assertEqual(len(s3), 2)
        self.assertEqual(len(s2),1)
        self.assertTrue(c3 in s2)
        self.assertFalse(c1 in s2)
        
    def test_pop(self):
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        c4 = Card(0, 3)
        
        s1 = s1 + c1 + c2 + c3 + c4
        
        c5 = s1.pop(0)
        self.assertTrue(isinstance(c5, Card))
        self.assertTrue(c5 == c1)
        self.assertEqual(len(s1), 3)
        
        c6 = Card(0,3)
        c7 = s1.pop(c6)
        self.assertTrue(isinstance(c7, Card))
        self.assertTrue(c7 == c6)
        self.assertEqual(len(s1), 2)
        
        self.assertRaises(IndexError, s1.pop, c1)
        
    def test_move(self):
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        c4 = Card(0, 3)
        
        s1 = s1 + c1 + c2 + c3 + c4
        c5 = Card(0,1)
        
        s1.move(0, s2)
        self.assertTrue(c5 in s1)
        s1.move(c5, s2)
        
        self.assertFalse( c1 in s1)
        self.assertFalse( c2 in s1)
        self.assertTrue( c1 in s2)
        self.assertTrue( c2 in s2)
        
    def test_empty(self):
        s1 = Stack()
        s2 = Stack()
                
        c1 = Card(0, 0)
        c2 = Card(0, 1)
        c3 = Card(0, 2)
        c4 = Card(0, 3)
        
        s1 = s1 + c1 + c2 + c3 + c4
        
        s2.cards = s1.cards[:]
        s1.empty()
        
        self.assertEqual(len(s1), 0)
        self.assertEqual(str(s1), 'is empty')
        
        with self.assertRaises(IndexError):
            s1[0]
        with self.assertRaises(IndexError):
            s1[-1]
            
        s1 = s1 - c1
        self.assertEqual(len(s1), 0)
        
        s2 = s2 + s1
        self.assertEqual(len(s2), 4)
        
if __name__=='__main__':
    unittest.main()
