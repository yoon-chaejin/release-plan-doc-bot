import os
import unittest

from docx import Document

from main import release_plan as rp
from main import release_plan_controller as rpc


class TestReleasePlanController(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)

    def test_create_daily_report(self):
        # given
        root_dir = os.getcwd()
        file_paths = [
            root_dir + "/resources/sample.docx",
            root_dir + "/resources/sample_copy.docx",
        ]
        release_plans = [rp.ReleasePlanFromDocxFile(i) for i in file_paths]

        # when
        # create_daily_report 호출
        daily_report = rpc.ReleasePlanController.create_daily_report(release_plans)

        # then
        self.assertIsInstance(daily_report, type(Document()))
        self.assertIsNotNone(daily_report.tables[0])

        self.assertEqual(len(daily_report.tables[0].rows), 3)
        self.assertEqual(len(daily_report.tables[0].columns), 2)

        self.assertEqual(daily_report.tables[0].cell(0, 0).text, "작업자")
        self.assertEqual(daily_report.tables[0].cell(0, 1).text, "작업 내용")

        self.assertEqual(
            daily_report.tables[0].cell(1, 0).text,
            release_plans[0].get_developer_name(),
        )
        self.assertEqual(
            daily_report.tables[0].cell(1, 1).text,
            release_plans[0].get_release_plan_description(),
        )
        self.assertEqual(
            daily_report.tables[0].cell(2, 0).text,
            release_plans[1].get_developer_name(),
        )
        self.assertEqual(
            daily_report.tables[0].cell(2, 1).text,
            release_plans[1].get_release_plan_description(),
        )


if __name__ == "__main__":
    unittest.main()
