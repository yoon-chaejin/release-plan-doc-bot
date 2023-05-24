import unittest
import os

from docx import Document

from main import file_controller as fc

class TestFileController(unittest.TestCase):
    
    @unittest.skip("User Input 테스트로 Skip")
    def test_get_file_paths(self):
        # given
        file_controller = fc.FileController()

        # when
        file_paths = file_controller.get_file_paths()

        # then
        self.assertIsInstance(file_paths, type([]))

    def test_save_document_as_docx_file(self):
        # given
        file_controller = fc.FileController()

        root_dir = os.getcwd()
        file_path = root_dir + '/resources/'
        file_name = 'sample_save.docx'
        document = Document()
        
        # when
        file_controller.save_document_as_docx_file(file_path, file_name, document)

        # then
        result_document = Document(file_path + file_name)
        self.assertNotEqual(result_document, None)

if __name__ == '__main__':
    unittest.main()