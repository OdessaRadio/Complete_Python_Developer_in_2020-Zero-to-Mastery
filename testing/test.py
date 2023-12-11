import unittest
import main1

class TestMain(unittest.TestCase):
    def setUp(self): # run another piece of code before each call of the test
        print("About test the function")

    def test_doStuff(self):
        '''arg = 10'''
        test_param = 10
        result = main1.doStuff(test_param)
        self.assertEqual(result, 15)

    def test_doStuff2(self):
        '''arg = "dfdff"'''
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

    def tearDown(self): # Run in the end of each method in test
        print("Cleaning up")


if __name__ == '__main__':
    unittest.main()