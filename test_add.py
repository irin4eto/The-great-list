import unittest

import add

import os

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.a = add.Add(1)
        self.file_name = "[1] HackBulgaria.txt"
        self.handle = open(self.file_name, "w")

    def test_get_file(self):
        self.assertEqual(self.file_name, self.a.get_file())

    def tearDown (self):
        os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
