import unittest
import main.file_controller as fc
from main.release_plan import ReleasePlan

class TestFileController(unittest.TestCase):

    def test_loadReleasePlanFromDocxFile(self):
        ##given
        file_path = './../resources/sample.docx'

        # when
        release_plan = fc.load_release_plan_from_docx_file(file_path)

        # then
        self.assertIs(type(release_plan), ReleasePlan)
    

if __name__ == '__main__':
    unittest.main()