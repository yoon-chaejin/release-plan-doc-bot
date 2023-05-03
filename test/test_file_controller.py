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