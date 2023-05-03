import unittest
import os
from main.release_plan import ReleasePlanFromDocxFile
from docx import Document

class TestMain(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(True, True)

    def test_create_daily_report(self):
        # given
        root_dir = os.getcwd()
        file_paths = [root_dir + '/resources/sample.docx', root_dir + '/resources/sample_copy.docx']
        release_plans = [ReleasePlanFromDocxFile(i) for i in file_paths]

        # when
        # create_daily_report 호출
        daily_report = create_daily_report(release_plans)
        
        # then
        self.assertIsInstance(daily_report, Document)
        # 파일 내 표가 있음
        # 파일 내 표는 row 3개, col 2개
        # 파일 내 표의 첫 번째 row 는 작업자 / 작업 내용


if __name__ == '__main__':
    unittest.main()