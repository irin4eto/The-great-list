import unittest

import search_email

import os

class TestSearchEmail(unittest.TestCase):

    def test_search_file(self):
        search = search_email.SearchEmail("irina.bs@abv.bg")

        file_name = "[1] FMI.txt"
        file_handler = open(file_name, 'w')
        file_handler.write("Irina Ivanova - irina.bs@abv.bg")
        file_handler.close()

        self.assertEqual(True, search.search_email())

        os.remove(file_name)

if __name__ == '__main__':
    unittest.main()


