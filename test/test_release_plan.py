import unittest
from main.release_plan import ReleasePlanFromDocxFile
import os

class TestReleasePlan(unittest.TestCase):

    def test_constructor_ReleasePlanFromDocxFile(self):
        ##given
        root_dir = os.getcwd()
        file_path = root_dir + '/resources/sample.docx'
        title = '제목DATA'
        request_id = 'CHYYMMDD-XXXXXX'

        file_path_copy = root_dir + '/resources/sample_copy.docx'
        title_copy = '제목DATA_COPY'

        # when
        release_plan = ReleasePlanFromDocxFile(file_path)
        release_plan_copy = ReleasePlanFromDocxFile(file_path_copy)

        # then
        self.assertEquals(release_plan.title, title)
        self.assertEquals(release_plan.request_id, request_id)

        self.assertEquals(release_plan_copy.title, title_copy)

if __name__ == '__main__':
    unittest.main()