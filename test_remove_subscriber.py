import unittest

import os

import remove_subscriber

class TestRemove(unittest.TestCase):

    def setUp(self):
        self.file_name = "[1] Hack Bulgaria.txt"
        self.file_writer = open(self.file_name, "w")
        self.removier = remove_subscriber.Remove(1, 'Irina Ivanova')

    def test_remove(self):
        self.file_writer.write("Irina Ivanova - irina.bs@abv.bg\n")
        self.file_writer.write("George Ivanov - george_ivanov@abv.bg")
        self.file_writer.close()

        self.removier.remove()
        file_reader = open(self.file_name, "r")

        self.assertEqual(file_reader.read(), "George Ivanov - george_ivanov@abv.bg")
        file_reader.close()

    def tearDown(self):
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()

