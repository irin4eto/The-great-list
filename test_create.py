import unittest

import create

import os


class TestCreate(unittest.TestCase):

    def test_create(self):
        self.c = create.Create("HackBulgaria")
        print(self.c.list_name)

        self.c.create()
        self.assertEqual(True, os.path.isfile(self.c.list_name))

        os.remove(self.c.list_name)

if __name__ == '__main__':
    unittest.main()


