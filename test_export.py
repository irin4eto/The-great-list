import unittest
import os

import export

class TestExport(unittest.TestCase):

    def setUp(self):
        self.file_name = "[1] HackBulgaria.txt"
        self.json_name = "[1] HackBulgaria.json"
        self.file_handle = open(self.file_name, "w")
        self.exporting = export.Export(1)

    def test_export(self):
        self.file_handle.write("Irina Ivanova - irina.bs@abv.bg")
        self.file_handle.close()

        self.exporting.export()

        self.assertEqual(True, os.path.isfile("[1] HackBulgaria.json"))

        file_reader = open(self.json_name, "r")
        contents = file_reader.read()
        file_reader.close()

        self.assertEqual(contents, "[\n{\n    \"email\": \" irina.bs@abv.bg\",\n    \"name\": \"Irina Ivanova \"\n}\n]")

    def tearDown(self):
        os.remove(self.file_name)
        os.remove(self.json_name)

if __name__ == '__main__':
    unittest.main()


