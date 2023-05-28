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
        developer_name = "개발자명DATA"
        release_plan_description = "목적/개선내용DATA"

        file_path_copy = root_dir + "/resources/sample_copy.docx"
        title_copy = "제목DATA_COPY"

        # when
        release_plan = rp.ReleasePlan.fromDocxFilePath(file_path)
        release_plan_copy = rp.ReleasePlan.fromDocxFilePath(file_path_copy)

        # then
        self.assertEqual(release_plan.title, title)
        self.assertEqual(release_plan.request_id, request_id)
        self.assertEqual(release_plan.developer_name, developer_name)
        self.assertEqual(
            release_plan.release_plan_description, release_plan_description
        )

        self.assertEqual(release_plan_copy.title, title_copy)


if __name__ == "__main__":
    unittest.main()
