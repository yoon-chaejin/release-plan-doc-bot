import unittest
import main.file_controller as fc
from main.release_plan import ReleasePlan

class TestFileController(unittest.TestCase):

    def test_loadReleasePlanFromDocxFile(self):
        ##given
        file_path = './../resources/sample.docx'
        title = '제목DATA'
        request_id = 'CHYYMMDD-XXXXXX'

        file_path_copy = './../resources/sample_copy.docx'
        title_copy = '제목DATA_COPY'

        # when
        release_plan = fc.load_release_plan_from_docx_file(file_path)
        release_plan_copy = fc.load_release_plan_from_docx_file(file_path_copy)

        # then
        self.assertIs(type(release_plan), ReleasePlan)
        self.assertEquals(release_plan.title, title)
        self.assertEquals(release_plan.request_id, request_id)

        self.assertEquals(release_plan_copy.title, title_copy)
    

if __name__ == '__main__':
    unittest.main()