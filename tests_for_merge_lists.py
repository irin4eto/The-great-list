import merge_lists
import unittest

class MergeListsTest(unittest.TestCase):

    def test_merge_lists(self):
        self.file1 = open('[1] Hack.txt', 'r')
        self.file2 = open('[2] Bulgaria.txt', 'r')
        self.content1 = self.file1.read()
        self.content2 = self.file2.read()
        self.content = self.content2 + self.content1
        my_unbelivable_object = merge_lists.MergeLists('[1] Hack.txt', '[2] Bulgaria.txt', 'New_list')
        my_unbelivable_object.merge_lists()
        self.the_new_file = open('[3] New_list.txt', 'r')
        self.conent_of_the_big_file = self.the_new_file.read()
        self.assertEqual(self.content , self.conent_of_the_big_file)

if __name__ == '__main__':
    unittest.main()
