import unittest

import create

import os


class TestCreate(unittest.TestCase):

    def test_create(self):
        creating = create.Create("HackBulgaria")

        creating.create()
        self.assertEqual(True, os.path.isfile(creating.list_name))

        os.remove(creating.list_name)

if __name__ == '__main__':
    unittest.main()


