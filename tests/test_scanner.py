import unittest
from scanner.utils import validate_port_range


class TestUtils(unittest.TestCase):

    def test_valid_range(self):
        self.assertEqual(validate_port_range("20-80"), (20, 80))

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            validate_port_range("80-20")


if __name__ == "__main__":
    unittest.main()