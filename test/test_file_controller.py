import unittest
import main.file_controller as fc
from main.release_plan import ReleasePlan

class TestFileController(unittest.TestCase):

    def test_loadReleasePlanFromDocxFile(self):
        ##given
        file_path = './../resources/sample.docx'
        title = '제목DATA'
        request_id = 'CHYYMMDD-XXXXXX'

        # when
        release_plan = fc.load_release_plan_from_docx_file(file_path)

        # then
        self.assertIs(type(release_plan), ReleasePlan)
        self.assertEquals(release_plan.title, title)
        self.assertEquals(release_plan.request_id, request_id)
    

if __name__ == '__main__':
    unittest.main()