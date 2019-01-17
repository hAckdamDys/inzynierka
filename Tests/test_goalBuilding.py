import unittest
import numpy as np
from SwarmBots.GoalBuilding import GoalBuilding


class TestGoalBuilding(unittest.TestCase):
    """Basic test cases."""

    def test_simple_grid(self):
        textGrid = """
        0 0 0 0 0 0 0
        0 0 0 1 0 0 0
        0 0 1 2 1 0 0
        0 1 2 3 2 1 0
        0 0 1 2 1 0 0
        0 0 0 1 0 0 0
        0 0 0 0 0 0 0
        """
        resultGrid = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 2, 1, 0, 0],
            [0, 1, 2, 3, 2, 1, 0],
            [0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        goalBuilding = GoalBuilding(textGrid)
        assert np.array_equal(goalBuilding.grid, resultGrid)


if __name__ == '__main__':
    unittest.main()
