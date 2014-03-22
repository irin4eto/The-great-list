import show_lists

class Remove():
    def __init__(self, list_identifier, name_identifier):
        if list_identifier > len(show_lists.ShowLists.show_lists()):
            self.list_identificier = 1
            print("Incorrect list identificier.Write new list identifier.")
            print("Another way removing will be made to the first list")
        else:
            self.list_identifier = list_identifier
        self.name_identifier = name_identifier

    def remove(self):
        all_lists = show_lists.ShowLists.show_lists()
        for file_list in all_lists:
            if str(self.list_identifier) in file_list:
                file_reader = open("{}.txt".format(file_list), "r")
                lines = file_reader.readlines()
                print(lines)
                file_reader.close()

                file_writer = open("{}.txt".format(file_list), "w")
                for line in lines:
                    if not self.name_identifier in line:
                        file_writer.write(line)
                file_writer.close()



