import unittest
from transformers.string import *

class TestTransformersMethodsForString(unittest.TestCase):

    def test_get_element_by_batch_of(self):
        self.assertEqual(ascii2octalstring('cat /chall/secret.txt'), r'\143\141\164\040\057\143\150\141\154\154\057\163\145\143\162\145\164\056\164\170\164')

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()