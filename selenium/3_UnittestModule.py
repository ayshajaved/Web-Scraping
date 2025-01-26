'''
unittest is an essential tool for ensuring the correctness of your code by allowing you 
to write tests for each unit of your program, ensuring that your code behaves as expected
and is free from errors. It is commonly used in both small-scale projects and large applications 
to improve code reliability.
'''
import unittest
#testing a simple add formula
def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):   
    #test case 1: test with positive numbers
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 7), 12)
    
    #test case 2: test with negative numbers
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -7), -12)

    #test case 3: test with mixed numbers
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 7), 2)

    #test case 4: test with zero
    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)
if __name__ == '__main__':
    unittest.main()

#printing ok if all test cases pass