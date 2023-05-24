import os
import unittest

from main import release_plan as rp


class TestReleasePlan(unittest.TestCase):
    def test_constructor_release_plan_from_docx_file(self):
        # given
        root_dir = os.getcwd()
        file_path = root_dir + "/resources/sample.docx"
        title = "제목DATA"
        request_id = "CHYYMMDD-XXXXXX"

        file_path_copy = root_dir + "/resources/sample_copy.docx"
        title_copy = "제목DATA_COPY"

        # when
        release_plan = rp.ReleasePlanFromDocxFile(file_path)
        release_plan_copy = rp.ReleasePlanFromDocxFile(file_path_copy)

        # then
        self.assertEqual(release_plan.title, title)
        self.assertEqual(release_plan.request_id, request_id)

        self.assertEqual(release_plan_copy.title, title_copy)

    def test_get_developer_name(self):
        # given
        root_dir = os.getcwd()
        file_path = root_dir + "/resources/sample.docx"
        developer_name = "개발자명DATA"

        # when
        release_plan = rp.ReleasePlanFromDocxFile(file_path)

        # then
        self.assertEqual(release_plan.get_developer_name(), developer_name)

    def test_get_release_plan_description(self):
        # given
        root_dir = os.getcwd()
        file_path = root_dir + "/resources/sample.docx"
        release_plan_description = "목적/개선내용DATA"

        # when
        release_plan = rp.ReleasePlanFromDocxFile(file_path)

        # then
        self.assertEqual(
            release_plan.get_release_plan_description(), release_plan_description
        )


if __name__ == "__main__":
    unittest.main()
