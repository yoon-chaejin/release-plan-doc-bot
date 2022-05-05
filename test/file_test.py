import unittest
from main.file import File

class FileTests(unittest.TestCase):
    def test_FileConstructor(self):
        sample_filename = "sample.docx"
        file = File(sample_filename)

        assert(file.filename, sample_filename)
