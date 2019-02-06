from SwarmBots.sharedGrid import SharedGrid
from unittest.mock import Mock
import pytest

@pytest.fixture(params=[3,4,5])
def sharedGrid(request):
    sharedGrid = SharedGrid(width=request.param, height=request.param)
    return sharedGrid


def test_buildingGridInitialization(sharedGrid):
    assert sharedGrid


def test_addNewTile(sharedGrid):
    tile = Mock
    assert sharedGrid.lastTileIndex == 0
    sharedGrid.addNewTile(tile)
    assert sharedGrid.lastTileIndex == 1

# def test_addTile(buildingGrid):
#

@pytest.mark.parametrize("x, y", (
        (0, 0),
        (1, 0),
        (0, 1),
))
def test_addRobot(sharedGrid, x, y):
    robot = Mock(x=x, y=y)
    assert not sharedGrid.positionFromRobot
    assert not sharedGrid.robotsGrid[x][y]
    sharedGrid.addRobot(robot)
    assert sharedGrid.positionFromRobot
    assert sharedGrid.robotsGrid[x][y]

# @pytest.mark.parametrize("nextX, nextY", (
#         (1, 0),
#         (0, 1),
# ))
# def test_moveRobot(sharedGrid, nextX, nextY):
#     robot = Mock(wantToMove=True, x=0, y=0)
#     sharedGrid.moveRobot(robot, nextX, nextY)
#     assert robot.x == nextX
#     assert robot.y == nextY

