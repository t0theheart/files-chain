from files_chain import FilesChain


def main():
    """
        Example of using

        "Files chain" started!
        Enter the file path: main.txt
        Обработчик "txt" получил файл "child_files/text.txt"
        Обработчик "json" получил файл "child_files/data.json"
        Обработчик "xml" получил файл "child_files/menu.xml"
        Обработчик "csv" получил файл "child_files/table.csv"
        End.
    """
    app = FilesChain()
    print('"Files chain" started!')
    read_from = input('Enter the file path: ')
    app.do_files_process(read_from=read_from)
    print('End.')


if __name__ == '__main__':
    main()
