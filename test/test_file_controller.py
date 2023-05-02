import unittest
from main.file_controller import FileController

class TestFileController(unittest.TestCase):
    
    def test_getFilePaths(self):
        # given
        fc = FileController()

        # when
        filePaths = fc.getFilePaths()

        # then
        self.assertIsInstance(filePaths, type([]))