import show_list
import unittest


class ShowListTests(unittest.TestCase):

    def setUp(self):
        self.my_file1 = show_list.ShowList("[1] Hack")
        self.my_file2 = show_list.ShowList("[2] Bulgaria")

    def test_show_list_with_no_content(self):
        self.assertEqual("", self.my_file1.show_the_list())

    def test_show_list_with_content(self):
        self.assertEqual("George Ivanov - ghost_vision@abv.bg\n", self.my_file2.show_the_list())

if __name__ == '__main__':
    unittest.main()
