import unittest
import main1

class TestMain(unittest.TestCase):
    def test_doStuff(self):
        test_param = 10
        result = main1.doStuff(test_param)
        self.assertEqual(result, 15)

    def test_doStuff2(self):
        test_param = 'dfdff'
        result = main1.doStuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_doStuff3(self):
        test_param = None
        result = main1.doStuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_doStuff4(self):
        test_param = ''
        result = main1.doStuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_doStuff5(self):
        test_param = 0
        result = main1.doStuff(test_param)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()