import show_lists
import sys
import os
import fileinput



class UpdateSubscriber():

    def __init__(self, list_identifier, name_identifier):
        self.list_identifier_number = list_identifier
        self.name_identifier_number = name_identifier
        self.list_identifier = "[" + list_identifier + "]"
        self.name_identifier = "[" + name_identifier + "]"

    def update_subsriber(self):
        lists = show_lists.ShowLists.show_lists()
        list_exists = False
        name_exists = False
        for i in lists:
            if self.list_identifier in i:
                list_exists = True
                filename = i + ".txt"
                file = open(filename, 'r')
                content = file.read()
                entries = content.split("\n")
                for name_and_email in entries:
                    if (self.name_identifier in name_and_email):
                        name_exists = True
                        print("Updating: " + name_and_email)
                        print("Press enter if you want the field to remain the same")
                        fields = name_and_email.split(" - ")
                        old_name = fields[0][3:]
                        old_email = fields[1]
                        new_name = input("Enter new name>")
                        new_email = input("Enter new email>")
                        if(new_name == ""):
                            name = old_name[1:]
                        else:
                            name = new_name
                        if(new_email == ""):
                            email = old_email
                        else:
                            email = new_email
                        new_entry = self.name_identifier + " "+ name + " - " + email
                        file_directory = os.getcwd() + "/" + filename
                        file.close()
                        exit_status_for_replace_in_file = UpdateSubscriber.replaceAll(filename, name_and_email, new_entry)
                        if exit_status_for_replace_in_file:
                            return ("Subscriber updated: " + new_entry)
                        else:
                            return ("No changes has been done to " + name_and_email)
                        break
                if not name_exists:
                    return ("Subscriber with identifider <" + self.list_identifier_number + "> was not found in the list <" + i[4:] + ">.")
        if not list_exists:
            return ("List with unique identifier <" + self.list_identifier_number + "> was not found.")


    def replaceAll(file,searchExp,replaceExp):
        for line in fileinput.input(file, inplace=1):
            if searchExp in line:
                line = line.replace(searchExp,replaceExp)
            sys.stdout.write(line)
        if(searchExp != replaceExp):
            return True
            #print("Subscriber updated: " + replaceExp)
        else:
            return False
            #print("No changes has been done to " + searchExp)


def main():
    test_object = UpdateSubscriber("1", "1")
    print ()
    print ()
    print (test_object.update_subsriber())
    print ()
    print ()

if __name__ == '__main__':
    main()

