import os

class Add():
    def __init__(self, list_identifier):
        self.list_identifier = list_identifier

    def add(self):
        name = input("name> ")
        email = input("email> ")
        file_name = get_file()
        file = open(file_name, "w")
        file.write("{} - {}".format(name,email))
        file.close()
        print("{} {} was added to {}".format(name, email, ))

    def get_file(self):
        all_files = os.listdir()
        for file_name in all_files:
            if str(self.list_identifier) in file_name:
                return file_name
