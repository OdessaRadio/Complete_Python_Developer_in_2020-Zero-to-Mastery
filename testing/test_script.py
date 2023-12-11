import unittest
import script

class TestMain(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_2(self):
        '''wrong guess'''
        answer = 5
        guess = 0
        result = script.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_3(self):
        '''number is higher than 10'''
        answer = 5
        guess = 11
        result = script.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_4(self):
        '''input is string'''
        answer = 5
        guess = '11'
        result = script.run_guess(guess, answer)
        #self.assertFalse(result)
        self.assertIsInstance(result, TypeError)

if __name__ == '__main__':
    unittest.main()