import unittest
from hw1 import choose

class TestHW1(unittest.TestCase):
    def test_main(self):
        test_cases = [
            ("Case 1", (25.0, 5.5, -0.1), "Lỗi input"),
            ("Case 2", (25.0, 5.5, 0.0), "Không thả gì"),
            ("Case 3", (25.0, 5.5, 0.1), "Không thả gì"),
            ("Case 4", (25.0, 5.5, 4.0), "Thả tôm"),
            ("Case 5", (25.0, 5.5, 5.4), "Thả cá"),
            ("Case 6", (25.0, 5.5, 5.5), "Thả cá"),
            ("Case 7", (25.0, 5.5, 5.6), "Lỗi input"),
            ("Case 8", (19.9, 5.5, 4.0), "Không thả gì"),
            ("Case 9", (20.0, 5.5, 4.0), "Không thả gì"),
            ("Case 10", (20.1, 5.5, 4.0), "Không thả gì"),
            ("Case 11", (29.9, 5.5, 4.0), "Thả tôm"),
            ("Case 12", (30.0, 5.5, 4.0), "Thả tôm"),
            ("Case 13", (30.1, 5.5, 4.0), "Lỗi input"),
            ("Case 14", (25.0, 3.9, 4.0), "Lỗi input"),
            ("Case 15", (25.0, 4.0, 4.0), "Thả tôm"),
            ("Case 16", (25.0, 4.1, 4.0), "Thả tôm"),
            ("Case 17", (25.0, 6.9, 4.0), "Thả tôm"),
            ("Case 18", (25.0, 7.0, 4.0), "Thả tôm"),
            ("Case 19", (25.0, 7.1, 4.0), "Lỗi input"),
        ]
        for case_id, args, expected in test_cases:
            with self.subTest(case=case_id, args=args):
                self.assertEqual(choose(*args), expected, msg=f"expected: {expected}, actual: {choose(*args)} in test case {case_id}")

if __name__ == "__main__":
    unittest.main()