import unittest
from main import QUESTIONS

class DigitalCitizenTests(unittest.TestCase):
    def test_question_bank(self):
        self.assertGreaterEqual(len(QUESTIONS), 5)
        for question, options, answer, explanation in QUESTIONS:
            self.assertIn(answer, range(len(options)))
            self.assertTrue(explanation)

if __name__ == "__main__":
    unittest.main()
