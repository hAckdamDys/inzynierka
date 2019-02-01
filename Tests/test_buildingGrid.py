from SwarmBots.buildingGrid import BuildingGrid
from unittest.mock import Mock
import pytest

@pytest.fixture(params=[3,4,5])
def buildingGrid(request):
    buildingGrid = BuildingGrid(width=request.param, height=request.param)
    return buildingGrid

def test_buildingGridInitialization(buildingGrid):
    assert buildingGrid

def test_addNewTile(buildingGrid):
    tile = Mock
    assert buildingGrid.lastTileIndex == 0
    buildingGrid.addNewTile(tile)
    assert buildingGrid.lastTileIndex == 1

# def test_addTile(buildingGrid):
#

@pytest.mark.parametrize("x, y", (
        (0, 0),
        (1, 0),
        (0, 1),
))
def test_addRobot(buildingGrid, x, y):
    robot = Mock(x=x, y=y)
    assert not buildingGrid.positionFromRobot
    assert not buildingGrid.robotsGrid[x][y]
    buildingGrid.addRobot(robot)
    assert buildingGrid.positionFromRobot
    assert buildingGrid.robotsGrid[x][y]

# @pytest.mark.parametrize("nextX, nextY", (
#         (1, 0),
#         (0, 1),
# ))
# def test_moveRobot(buildingGrid, nextX, nextY):
#     robot = Mock(wantToMove=True, x=0, y=0)
#     buildingGrid.moveRobot(robot, nextX, nextY)
#     assert robot.x == nextX
#     assert robot.y == nextY

