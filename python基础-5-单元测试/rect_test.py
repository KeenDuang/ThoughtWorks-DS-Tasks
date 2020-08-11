import unittest

from rect import Rect


class RectTest(unittest.TestCase):
    def test_intersect_for_crossing_rects(self):
        self.assertTrue(Rect(0, 0, 2, 2).intersect(Rect(1, -1, 2, 2)))

    def test_intersect_for_nocrossing_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, -1, 2, 0.5)))

    def test_intersect_for_nocrossing_rects_(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(-1, -1, 1, 1)))


if __name__ == '__main__':
    unittest.main()
