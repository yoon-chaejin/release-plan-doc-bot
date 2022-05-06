import unittest
from main.file import File

class FileTests(unittest.TestCase):
    
    def test_FileConstructor(self):
        SAMPLE_FILE_ROUTE = "./resources/sample.docx"
        file = File(SAMPLE_FILE_ROUTE)

        self.assertEqual(file.filename, SAMPLE_FILE_ROUTE.split('/')[-1])
