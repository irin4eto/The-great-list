import os

import show_lists

class Add():
    def __init__(self, list_identifier):
        if list_identifier > len(show_lists.ShowLists.show_lists()):
            self.list_identifier = 1
            print("Incorrect list identificier.People will be added to first list")
        else:
            self.list_identifier = list_identifier

    def add(self):
        name = input("name> ")
        email = input("email> ")
        file_name = self.get_file()
        file = open(file_name, "w")
        file.write("{} {} - {}".format(self.find_person_identicier, name, email))
        file.close()
        print("{} {} was added to {}".format(name, email, ))

    def get_file(self):
        all_files = os.listdir()
        for file_name in all_files:
            if str(self.list_identifier) in file_name:
                return file_name

    def find_person_identificier(self):
        file_name = self.get_file()
        person_identificier = 1
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()
        last_line = lines[len(lines) - 1]
        if len(lines) > 0:
            person_identificier = int(last_line[1]) + 1
        return person_identificier



