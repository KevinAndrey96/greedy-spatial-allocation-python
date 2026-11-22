"""
Unit tests for the Bird Nest Allocation Algorithm
"""

import unittest
from main import longest_false_run, occupy_step, simulate_occupy


class TestNests(unittest.TestCase):

    def test_longest_false_run(self):
        # [True, False, False, True, False] -> longest run is index 1, len 2
        start, length = longest_false_run([True, False, False, True, False])
        self.assertEqual(start, 1)
        self.assertEqual(length, 2)

    def test_occupy_step_sequence(self):
        nests = [False] * 10
        first_idx = occupy_step(nests)
        self.assertEqual(first_idx, 5)
        self.assertTrue(nests[5])

        second_idx = occupy_step(nests)
        self.assertEqual(second_idx, 2)
        self.assertTrue(nests[2])

        third_idx = occupy_step(nests)
        self.assertEqual(third_idx, 8)
        self.assertTrue(nests[8])

    def test_full_simulation(self):
        n = 5
        steps = simulate_occupy(n)
        self.assertEqual(len(steps), n + 1)
        self.assertEqual(steps[0], "_ _ _ _ _")
        self.assertEqual(steps[-1], "X X X X X")


if __name__ == '__main__':
    unittest.main()
