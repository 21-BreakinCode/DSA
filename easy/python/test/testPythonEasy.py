import unittest

from twoSum.twoSum import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.TwoSum = TwoSum()

    def test_general(self):
        nums = [2, 7, 11, 15]
        target = 9

        result = self.TwoSum.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_same_number(self):
        nums = [3, 3]
        target = 6

        result = self.TwoSum.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_unsorted_list(self):
        nums = [3, 2, 4]
        target = 6

        result = self.TwoSum.twoSum(nums, target)
        self.assertEqual(result, [1, 2])

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8

        result = self.TwoSum.twoSum(nums, target)
        self.assertEqual(result, [2, 4])

