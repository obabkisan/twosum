import unittest

def f(nums, target):
    if len(nums) < 2:
        return None

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

class TestTwoSum(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(f([2, 7, 11, 15], 9), (0, 1))

    def test_example2(self):
        self.assertEqual(f([3, 2, 4], 6), (1, 2))

    def test_example3(self):
        self.assertEqual(f([3, 3], 6), (0, 1))

    def test_no_solution(self):
        self.assertIsNone(f([1, 2, 3], 100))

    def test_minimal_pair(self):
        self.assertEqual(f([1, 3, 2, 2], 4), (0, 1))

    def test_duplicates(self):
        self.assertEqual(f([1, 1, 1, 1], 2), (0, 1))

    def test_large_numbers(self):
        big = 10**9
        self.assertEqual(f([big, -big], 0), (0, 1))

    def test_minimum_length(self):
        self.assertIsNone(f([5], 5))

    def test_negative_target(self):
        self.assertEqual(f([-3, -2, -7], -5), (0, 1))

if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)