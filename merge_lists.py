import create


class MergeLists():

    def __init__(self, list1, list2, new_list):
        self.list1 = list1
        self.list2 = list2
        self.new_list = new_list

    def merge_lists(self):
        new_object_list  = create.Create(self.new_list)
        self.the_last_file = new_object_list.create()
        self.my_file = open(self.the_last_file, 'a')
        self.file1 = open(self.list1, 'r')
        self.content1 = self.file1.read()
        self.file2 = open(self.list2, 'r')
        self.content2 = self.file2.read()
        self.content = self.content2 + self.content1
        self.my_file.write(self.content)
        self.my_file.close()
        self.file1.close()
        self.file2.close()

def main():
    strange_object = MergeLists('[1] Hack.txt', '[2] Bulgaria.txt', 'My_new_list')
    strange_object.merge_lists()

if __name__ == '__main__':
    main()
