import unittest
from hw1_fixed import choose

class TestHW1(unittest.TestCase):
    def test_main(self):
        test_cases = [
            ("Case 1", (10, 10, 10), "Lỗi input"),
            ("Case 2", (25, 1, 10), "Lỗi input"),
            ("Case 3", (25, 5.5, -10), "Lỗi input"),
            ("Case 4", (27, 6.5, 4.5), "Thả bạch tuộc"),
            ("Case 5", (25, 5.5, 4.5), "Thả cá"),
            ("Case 6", (25, 4, 3), "Thả tôm"),
            ("Case 7", (24, 5, 3), "Không thả gì"),
        ]
        for case_id, args, expected in test_cases:
            with self.subTest(case=case_id, args=args):
                self.assertEqual(choose(*args), expected, msg=f"expected: {expected}, actual: {choose(*args)} in test case {case_id}")

if __name__ == "__main__":
    unittest.main()