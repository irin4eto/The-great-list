import os


class ShowLists:
    @staticmethod
    def show_lists():
        directory_content = os.listdir()
        files = []
        length = 0
        for i in directory_content:
            if ".txt" in i and "[" in i and "~" not in i:
                length = len(i)
                files.append(i[:length-4])
        return files

def main():
    my_show = ShowLists()
    print(my_show.show_lists())

if __name__ == '__main__':
    main()


