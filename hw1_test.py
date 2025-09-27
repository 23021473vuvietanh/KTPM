import unittest
from hw1 import choose

class TestHW1(unittest.TestCase):
    def test_main(self):
        test_cases = [
            ((2, 3, 5), "Lỗi input"),          
            ((28, 6.5, 4.5), "Thả bạch tuộc"),
            ((26, 5.5, 5), "Thả cá"),          
            ((25, 4.5, 3.5), "Thả tôm"),      
        ]
        for args, expected in test_cases:
            with self.subTest(args=args):
                self.assertEqual(choose(*args), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)