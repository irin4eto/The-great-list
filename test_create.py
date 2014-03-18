import unittest

import create

import os


class TestCreate(unittest.TestCase):
    def setUp(self):
        self.c = create.Create("HackBulgaria")

    def test_create(self):
        self.c.create()
        self.assertEqual(True, os.path.isfile(self.c.list_name))

    def tearDown(self):
        os.remove(self.c.list_name)

if __name__ == '__main__':
    unittest.main()


