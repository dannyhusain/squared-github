import unittest2 as ut;
import mt;

class knownValues(ut.TestCase):
    def test10(self):
        result = mt.power(10);
        expected = 100;
        
        self.assertEqual(expected, result);
        
    def test5(self):
        result = mt.power(5);
        expected = 25;
        
        self.assertEqual(expected, result);
        
    def test1(self):
        result = mt.power(1);
        expected = 1;
        
        self.assertEqual(expected, result);
        
    def testNeg2(self):
        result = mt.power(-2);
        expected = 4;
        
        self.assertEqual(expected, result);
        
    def testNeg13(self):
        result = mt.power(13);
        expected = 169;
        
        self.assertEqual(expected, result);
        
if __name__ == '__main__':
    ut.main();