import show_lists

class SearchEmail():
    def __init__(self, email):
        self.email = email

    def search_email(self):
        all_lists = show_lists.ShowLists.show_lists()
        for file_list in all_lists:
            file_name = "{}.txt".format(file_list)
            file_handler = open(file_name, 'r')
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



