import unittest
from Dynamic import memo_knapsack
from greedy import FractionalKnapSack
from brute_knapsack import brute_knapsack
from kanp_Frac import knapSack_Fract



class Knapsack_test(unittest.TestCase):
    def test_greedy(self):
        
        val = [2,4,3,5,5]
        wt = [3,4,1,2,6]
        W = 12
        output = 15.666666666666666


        input = FractionalKnapSack.getMaxValue(wt, val, W)


        self.assertEqual(input, output)
    
    def test_bruteforce(self):
        val = [2,4,3,5,5]
        wt = [3,4,1,2,6]
        W = 12
        n = len(val)
        output = 15
        input = brute_knapsack(W, wt, val, n)
        self.assertEqual(input, output)
    
    def test_dymnamic(self):
        val = [2,4,3,5,5]
        wt = [3,4,1,2,6]
        W = 12
        n = len(val)
        output = 15
        input = memo_knapsack(wt, val, W, n)
        self.assertEqual(input, output)
    
    def test_fractional_Bruteforce(self):
        val = [2,4,3]
        wt = [3,4,1]
        W = 5
        n = len(val)
        input = knapSack_Fract(W, wt, val, n)
        output = 7
        self.assertEqual(input, output)


    


if __name__ == "__main__":
    unittest.main()
