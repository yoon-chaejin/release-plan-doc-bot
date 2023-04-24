import unittest

class TestMain(unittest.TestCase):

    def test_sample(self):

        print("""샘플 테스트""")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()