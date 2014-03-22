import show_lists
import os


class RemoveList():

    def __init__(self, list_identifier):
        self.list_identifier_number = list_identifier
        self.list_identifier = "[" + str(list_identifier) + "]"

    def remove_list(self):
        lists = show_lists.ShowLists.show_lists()
        list_exists = False
        for i in lists:
            if(self.list_identifier in i):
                list_exists = True
                print("Are you sure you want to delete <" + i[4:] + ">?")
                filename = i + ".txt"
                while True:
                    choise = input("Y/N>")
                    if choise == "Y" or choise == "y":
                        os.remove(filename)
                        print ("<" + i[4:] + "> was deleted.")
                        break
                    elif choise == "N" or choise == "n":
                        print("You crazy bastard. Stop playing with fire!")
                        break
                    else:
                        print("Wrong letter! Try again!")
        if not list_exists:
            print ("List with unique identifier <" + str(self.list_identifier_number) + "> was not found.")



def main():
    test_object = RemoveList(3)
    print(test_object.remove_list())

if __name__ == '__main__':
    main()
