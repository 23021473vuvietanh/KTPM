import unittest
from hw1 import choose

class TestHW1(unittest.TestCase):
    def test_main(self):
        test_cases = [
            ("Case 1", (-36, 6.3, 3.6), "Lỗi input"),
            ("Case 2", (20, 6.0, 4.0), "Không thả gì"),
            ("Case 3", (25, 6.3, 2.5), "Không thả gì"),
            ("Case 4", (26, 4.0, 4.0), "Thả tôm"),
            ("Case 5", (26, 6.0, 3.6), "Thả tôm"),
            ("Case 6", (26, 6.0, 5.0), "Thả cá"),
            ("Case 7", (26, 7.0, 5.0), "Thả cá"),
            ("Case 8", (28, 7.0, 5.0), "Thả bạch tuộc"),
        ]
        for case_id, args, expected in test_cases:
            with self.subTest(case=case_id, args=args):
                self.assertEqual(choose(*args), expected, msg=f"expected: {expected}, actual: {choose(*args)} in test case {case_id}")

if __name__ == "__main__":
    unittest.main()