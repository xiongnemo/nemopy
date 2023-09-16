import unittest
from parsers import PortRange

class TestPortRange(unittest.TestCase):

    def test_portrange_add(self):
        pr1 = PortRange('80,443,8080-8090')
        self.assertIn(80, pr1)
        self.assertIn(443, pr1)
        self.assertIn(8080, pr1)
        self.assertIn(8090, pr1)
        self.assertIn(8081, pr1)
        self.assertNotIn(8079, pr1)
        pr2 = PortRange('9,7070-6060,3')
        self.assertIn(9, pr2)
        self.assertIn(7070, pr2)
        self.assertIn(6060, pr2)
        self.assertIn(3, pr2)
        self.assertNotIn(7071, pr2)
        self.assertIn(6061, pr2)
        self.assertNotIn(2, pr2)

    def test_portrange_update(self):
        pr1 = PortRange('80,443,8080-8090')
        pr1.update('8081,8079')
        self.assertIn(8080, pr1)
        self.assertIn(8081, pr1)
        self.assertIn(8079, pr1)
        pr2 = PortRange('9,7070-6060,3')
        pr2.update('7071,6061,2')
        self.assertIn(7071, pr2)
        self.assertIn(6061, pr2)
        self.assertIn(2, pr2)



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
