import unittest
from files_chain import FilesChain
from files_chain.files_chain import FileHandlers


class TestMatricesGenerator(unittest.TestCase):

    def test_get_handler_txt(self):
        app = FilesChain()
        name, handler = app._get_handler('test.txt')
        self.assertEqual(name, 'txt')
        self.assertEqual(handler is FileHandlers.txt.value, True)

    def test_get_handler_csv(self):
        app = FilesChain()
        name, handler = app._get_handler('test.csv')
        self.assertEqual(name, 'csv')
        self.assertEqual(handler is FileHandlers.csv.value, True)

    def test_get_handler_xml(self):
        app = FilesChain()
        name, handler = app._get_handler('test.xml')
        self.assertEqual(name, 'xml')
        self.assertEqual(handler is FileHandlers.xml.value, True)

    def test_get_handler_json(self):
        app = FilesChain()
        name, handler = app._get_handler('test.json')
        self.assertEqual(name, 'json')
        self.assertEqual(handler is FileHandlers.json.value, True)
