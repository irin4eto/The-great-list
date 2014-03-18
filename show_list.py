import show_lists


class ShowList():

    def __init__(self, identifier):
        self.identifier = identifier

    def show_the_list(self):
        self.files = show_lists.ShowLists.show_lists()
        self.filename = ""
        for i in self.files:
            if ( self.identifier in i):
                self.filename = i + ".txt"
        self.file = open(self.filename, "r")
        self.content = self.file.read()
        return self.content
