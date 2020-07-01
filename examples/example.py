from files_chain import FilesChain


def main():
    app = FilesChain()
    app.do_files_process(read_from='main.txt')


if __name__ == '__main__':
    main()
