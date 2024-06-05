# test/test_coreFunc.py

import unittest
from foo_param.coreFunc import calculate_volume

class TestCore(unittest.TestCase):
    def test_calculate_volume(self):
        self.assertAlmostEqual(calculate_volume(1), 4.18879, places=5)
        self.assertAlmostEqual(calculate_volume(0), 0)
        with self.assertRaises(ValueError):
            calculate_volume(-1)


if __name__ == '__main__':
    unittest.main()