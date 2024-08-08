import unittest
from utils import generate_password

class TestUtils(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()
