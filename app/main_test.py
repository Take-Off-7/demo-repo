import os
import unittest
from main import return_backward_string, get_mode_value

# Set environment variable for testing
os.environ["APP_MODE"] = "test"

class TestFunctions(unittest.TestCase):

    def test_return_backward_string(self):
        self.assertEqual(return_backward_string("hello"), "olleh")
        self.assertEqual(return_backward_string("12345"), "54321")
        self.assertEqual(return_backward_string(""), "")

    def test_get_mode_value(self):
        self.assertEqual(get_mode_value(), "test")
        # del os.environ["APP_MODE"]
        self.assertEqual(get_mode_value(), "development")

if __name__ == "__main__":
    unittest.main()
