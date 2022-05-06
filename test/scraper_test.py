import unittest
from main.file import File
from main.release_plan_doc import ReleasePlanDoc
from main.scraper import FileScraper

class ScraperTests(unittest.TestCase): 

    def test_fileScraper(self):
        SAMPLE_FILE_ROUTE = "./resources/sample.docx"
        
        result = FileScraper.scrape(FileScraper, File(SAMPLE_FILE_ROUTE))

        self.assertIsInstance(result, ReleasePlanDoc)
        self.assertEqual(result.title, "제목DATA")
        self.assertEqual(result.working_time, "YYYY-MM-DD~YYYY-MM-DD")
        self.assertEqual(result.release_time, "YYYY-MM-DD  HH:MI ~ HH:MI")
        self.assertEqual(result.request_corporation, "고객사명DATA")
        self.assertEqual(result.request_group, "요청부서DATA")
        self.assertEqual(result.request_person, "요청자DATA")
        self.assertEqual(result.sor_id, "CHYYMMDD-XXXXXX")
        self.assertEqual(result.target_service, "시스템명DATA")
        self.assertEqual(result.risk_level, "3")
        self.assertEqual(result.response_group, "소속부서명DATA")
        self.assertEqual(result.developer, "개발자명DATA")
        self.assertEqual(result.task, "목적/개선내용DATA")