import unittest
from iterables import *

class TestIterablesMethods(unittest.TestCase):

    def test_get_element_by_batch_of(self):
        self.assertEqual(list(get_element_by_batch_of([1, 2, 3], 2)), [[1, 2], [3]])

    def test_chain_iterables(self):
        self.assertEqual(list(chain_iterables([1, 2], [3])), [1, 2, 3])

    def test_n_digit_suffix_generator(self):
        self.assertIn('0000', n_digit_suffix_generator(4))
        self.assertIn('8888', n_digit_suffix_generator(4))
        self.assertIn('9999', n_digit_suffix_generator(4))
        self.assertIn('0', n_digit_suffix_generator(1))

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()