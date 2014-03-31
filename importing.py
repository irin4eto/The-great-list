import show_lists
import json


class Importing():
    def __init__(self, json_list):
        self.json_list = json_list

    def importing(self):
        json_handle = open(self.json_list, 'r')
        json_content = json.load(json_handle)
        json_handle.close()

        list_identifier = len(show_lists.ShowLists.show_lists()) + 1
        file_name = "[{}] {}.txt".format(list_identifier, self.json_list[0:len(self.json_list) - 5])

        file_handle = open(file_name, 'w')
        for person in json_content:
            file_handle.write(person["name"] + "-")
            file_handle.write(person["email"] + "\n")
        file_handle.close()

