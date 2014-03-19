import show_lists

class SearchEmail():
    def __init__(self, email):
        self.email = email

    """def search_email(self):
        all_lists = show_lists.ShowLists.show_lists()
        print(all_lists)
        for file_list in all_lists:
            file_names = "{}.txt".format(file_list)
            print(file_names)
            file_handler = open(file_names, "r")
            print(self.email)
            print(file_handler.read() + "1")
            if self.email in file_handler.read():
                file_handler.close()
                return True
            else:
                file_handler.close()
        return False"""

    def search_email(self):
        all_lists = show_lists.ShowLists.show_lists()
        "print(all_lists)"
        for file_list in all_lists:
            file_name = "{}.txt".format(file_list)
            "print(file_name)"
            file_handler = open(file_name, 'r')
            "print(file_handler.read())"
            if self.email in file_handler.read():
                file_handler.close()
                return True
        file_handler.close()
        return False

def main():
    s = SearchEmail("irina.bs@abv.bg")
    print(s.search_email())

if __name__ == '__main__':
    main()



