import show_lists

class Create():
    def __init__(self, list_name):
        self.next_number = len(show_lists.ShowLists.show_lists()) + 1
        self.list_name = "[{}] {}{}".format(self.next_number, list_name, ".txt")

    def create(self):
        file = open(self.list_name, "w")
        file.close()
        return self.list_name
