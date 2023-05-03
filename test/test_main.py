import unittest

class TestMain(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(True, True)

    def test_create_daily_report(self):
        pass
        # given
        # input으로 다음 2개 file이 들어왔다고 가정
        # ['/Users/choijaeyoung/Desktop/yoon-chaejin-dev/release-plan-doc-bot/resources/sample_copy.docx', '/Users/choijaeyoung/Desktop/yoon-chaejin-dev/release-plan-doc-bot/resources/sample.docx']
        
        # when
        # create_daily_report 호출
        
        # then
        # output 으로 docx 파일이 생성됨
        # 파일 내 표가 있음
        # 파일 내 표는 row 3개, col 2개
        # 파일 내 표의 첫 번째 row 는 작업자 / 작업 내용


if __name__ == '__main__':
    unittest.main()