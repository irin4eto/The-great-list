import show_lists
import unittest


class ShowListsTest(unittest.TestCase):


    def test_show_lists(self):
        self.assertEqual(["[1] Hack"], show_lists.ShowLists.show_lists())

if __name__ == '__main__':
    unittest.main()
