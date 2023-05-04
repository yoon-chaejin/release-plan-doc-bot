import unittest
from main.file_controller import FileController

class TestFileController(unittest.TestCase):
    
    @unittest.skip("User Input 테스트로 Skip")
    def test_get_file_paths(self):
        # given
        file_controller = FileController()

        # when
        file_paths = file_controller.get_file_paths()

        # then
        self.assertIsInstance(file_paths, type([]))

    def test_save_document_as_docx_file(self):
        # given
        # file_path, file_name, document 가 주어졌을 때
        
        # when
        # document 저장

        # then
        # file_path + file_name 에 파일이 있는지
        pass