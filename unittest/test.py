import unittest




class SimpleClass:
   def __init__(self, value):
       self.value = value


   def add(self, other):
       """
       Add a value
       """
       return self.value + other


   def multiply(self, other):
       """
       Multiple a value
       """
       return self.value * other




""" Test 1 function ben ngoai"""
def test_random_func(x) -> int:
   return x + 3




class TestSimpleClass(unittest.TestCase):
   """
   Note: Class and functions must start with name Tests"""
   def setUp(self) -> None:
       # Create an instance of SimpleClass with a default value of 5 before each test
       self.obj = SimpleClass(5)


   def test_add(self):
       # Compare with 8
       self.assertEqual(self.obj.add(3), 8, "Addition method failed")


   def test_multiply(self):
       self.assertEqual(self.obj.multiply(4), 20, "Multiplication method failed")


   def test_random_func(self):
       self.assertEqual(test_random_func(4), 7, "Random function failed")


if __name__ == '__main__':
   # Run the unit tests
   unittest.main()
