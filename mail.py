import show_lists, show_list, add, remove_subscriber, update_subscriber
import create, update, search_email, merge_lists, export, importing, remove_list


def maillist():
    print("Hello Stranger! This is a cutting-edge, console-based mail-list!")
    print("Write command which you want!")
    while True:
        choice = input("Enter command> :")
        choices = choice.split(" ")
        if choices[0] == "show_lists":
            print(show_lists.ShowLists.show_lists())
        if choices[0] == "show_list":
            print(show_list.ShowList(choices[1]).show_list())
        if choices[0] == "add":
            add.Add([choices[1]]).add()
        if choices[0] == "update_subscriber":
            print(update_subscriber.UpdateSubscriber(choices[1], choices[2]).update_subscriber())
        if choices[0] == "remove_subscriber":
            print(remove_subscriber.Remove(choices[1], choices[2]).remove())
        if choices[0] == "create":
            create.Create(choices[1]).create()
        if choices[0] == "update":
            print(update.Update(choices[1], choices[2]).update())
        if choices[0] == "search_email":
            print(search_email.Search_Email([choices[1]]).search_email())
        if choices[0] == "merge_lists":
            print(merge_lists.MergeLists(choices[1], choices[2], choices[3]).merge_lists())
        if choices[0] == "export":
            print(export.Export(choices[0]).export())
        if choices[0] == "import":
            print(importing.Importing(choices[0]).importing())
        if choices[0] == "remove_list":
            print(remove_list.RemoveList(choices[0]).remove_list())
        if choices[0] == "exit":
            break
