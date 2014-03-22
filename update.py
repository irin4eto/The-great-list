import os
import show_lists

class Update():
    def __init__(self, list_identifier, new_list_name):
        self.list_identifier = list_identifier
        self.new_list_name = new_list_name

    def update(self):
        lists = show_lists.ShowLists.show_lists()
        checker_for_existence_of_identifier = False
        list_identifier_with_brackets = "[" + str(self.list_identifier) + "]"
        for i in lists:
            if list_identifier_with_brackets in i:
                checker_for_existence_of_identifier = True
                list_name = i
                break
        if not checker_for_existence_of_identifier:
            return ("List with unique identifier <" + list_identifier + "> not found")
        list_name_with_ext = list_name + ".txt"
        new_list_name_with_ext = "[" + str(self.list_identifier) + "] " + self.new_list_name + ".txt"
        os.rename(list_name_with_ext, new_list_name_with_ext)
        if (list_name[4:] == self.new_list_name):
            return ("The name remained the same: <" + list_name[4:] + ">")
        else:
            return ("Updated <" + list_name[4:] + "> to <" + self.new_list_name + ">.")

# def main():
#     test_object = Update(1, "Hack")
#     print (test_object.update())

# if __name__ == '__main__':
#     main()
