import unittest
import os
import importing


class TestImporting(unittest.TestCase):
    def setUp(self):
        self.json_name = "HackBulgaria.json"
        self.file_name = "[1] HackBulgaria.txt"
        self.json_handle = open(self.json_name, "w")
        self.i = importing.Importing(self.json_name)

    def test_importing(self):
        self.json_handle.write("[\n{\n    \"email\": \" irina.bs@abv.bg\",\n    \"name\": \"Irina Ivanova \"\n}\n]")
        self.json_handle.close()

        self.i.importing()

        self.assertEqual(True, os.path.isfile("[1] HackBulgaria.txt"))

        file_handle = open(self.file_name, 'r')
        content = file_handle.read()
        file_handle.close()

        self.assertEqual(content, "Irina Ivanova - irina.bs@abv.bg\n")

    def tearDown(self):
        os.remove(self.file_name)
        os.remove(self.json_name)

if __name__ == '__main__':
    unittest.main()
