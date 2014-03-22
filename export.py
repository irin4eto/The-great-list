import show_lists
import json

class Export():
    def __init__(self, list_identificier):
        if list_identificier > len(show_lists.ShowLists.show_lists()):
            self.list_identificier = 1
            print("Incorrect list identificier.Write new list identifier.")
            print("Another way exporting will be made to the first list")
        else:
            self.list_identificier = list_identificier

    def export(self):
        all_lists = show_lists.ShowLists.show_lists()
        for file_list in all_lists:
            if str(self.list_identificier) in file_list:
                file_handler = open("{}.txt".format(file_list), "r")
                json_handler = open("{}.json".format(file_list), "w")
                json_handler.write("[\n")
                for file_lines  in file_handler:
                    name = file_lines.split("-")[0]
                    email = file_lines.split("-")[1]
                    json_content = json.dumps({"name" : name, "email" : email},
                        sort_keys = True, indent = 4, separators=(',', ': '))
                    json_handler.write(json_content)
                json_handler.write("\n]")
                json_handler.close()
                file_handler.close()

def main():
    e = Export(1)
    e.export()

if __name__ == '__main__':
    main()

