import unittest

import add

import os

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.file_name = "[1] HackBulgaria.txt"
        self.handler = open(self.file_name, "w")
        self.a = add.Add(1)

    def test_get_file(self):
        self.assertEqual(self.file_name, self.a.get_file())

    def test_find_person_identificier(self):
        self.handler.write("[1] Irina Ivanova - irina.bs@abv.bg")
        self.handler.close()
        self.assertEqual(2, self.a.find_person_identificier())


    def tearDown (self):
        os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
