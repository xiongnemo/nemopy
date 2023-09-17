import unittest
from cls import DotDict

class TestDotDict(unittest.TestCase):
    
    def test_dotdict_add(self):
        a = DotDict({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
        self.assertIn('first_name', a)
        self.assertIn('last_name', a)
        self.assertIn('age', a)
        self.assertIn('sports', a)

    def test_dotdict_dot_attr_access(self):
        a = DotDict({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
        self.assertEqual(a.first_name, 'Eduardo')
        self.assertEqual(a.last_name, 'Pool')
        self.assertEqual(a.age, 24)
        self.assertEqual(a.sports, ['Soccer'])

    def test_dotdict_nested_dot_attr_access(self):
        d = DotDict({'a': {'b': {'c': 1}}})
        self.assertEqual(d.a.b.c, 1)



    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()