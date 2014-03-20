import unittest
import os

import export

class TestExport(unittest.TestCase):

    def test_export(self):
        exporting = export.Export(1)

        filename = "[1] HackBulgaria.txt"
        filehandler = open(filename, "w")
        filehandler.write("Irina Ivanova - irina.bs@abv.bg")
        filehandler.close()

        self.assertEqual(True, os.path.isfile("[1] HackBulgaria.json"))

        file_reader = open("[1] HackBulgaria.json", "r")
        contents = file_reader.read()
        file_reader.close()

        self.assertEqual(contents, "[\n{\n    \"email\": \" irina.bs@abv.bg\",\n    \"name\": \"Irina Ivanova \"\n}\n]")
if __name__ == '__main__':
    unittest.main()


