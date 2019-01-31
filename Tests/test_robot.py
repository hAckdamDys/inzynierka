import pytest
from unittest.mock import MagicMock
from SwarmBots.Robot import Robot

@pytest.fixture(params=[0,1,2,3])
def robot(request):
        buildingGrid = MagicMock
        buildingGrid.__init__.return_value = '[[0, 0, 0]' \
                                             '[0, 0, 0]' \
                                             '[0, 0, 0]]'

        robot = Robot(0, 0, buildingGrid, buildingGrid, rotation=request.param)
        return robot

def test_robotInitialization(robot):
    assert robot

@pytest.mark.parametrize("updateX, updateY", (
        (0, 0),
        (1, 0),
        (0, 1)
))
def test_updatePosition(robot, updateX, updateY):
    robot.wantToMove = True
    robot.updatePosition(updateX, updateY)
    assert robot.__eq__(Robot(updateX, updateY, 0, 0, 0))

@pytest.mark.parametrize("errorUpdateX, errorUpdateY", (
    (2, 0),
    (0, 2),
    (1, 1)
))
def test_updatePositionWithErrorParameters(robot, errorUpdateX, errorUpdateY):
    robot.wantToMove = True
    with pytest.raises(ValueError):
        robot.updatePosition(errorUpdateX, errorUpdateY)
    assert robot.__eq__(Robot(0, 0, 0, 0, 0))

@pytest.mark.parametrize("numberOfRightRotates, currentRotationForRightRotates", (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 0),
        (5, 1)
))
def test_rotate_right(numberOfRightRotates, currentRotationForRightRotates):
    robot = Robot(0,0,0,0,0)
    while numberOfRightRotates > 0:
        robot.rotateRight()
        numberOfRightRotates -= 1
    assert robot.currentRotation == currentRotationForRightRotates

@pytest.mark.parametrize("numberOfLeftRotates, currentRotationForLeftRotates", (
        (0, 0),
        (1, 3),
        (2, 2),
        (3, 1),
        (4, 0),
        (5, 3)
))
def test_rotate_left(numberOfLeftRotates, currentRotationForLeftRotates):
    robot = Robot(0, 0, 0, 0, 0)
    while numberOfLeftRotates > 0:
        robot.rotateLeft()
        numberOfLeftRotates -= 1
    assert robot.currentRotation == currentRotationForLeftRotates

def test_eq(robot):
    robot2 = Robot(0, 0, 0, 0, 0)
    assert robot.__eq__(robot2)

def test_notEq(robot):
    robot2 = Robot(1, 0, 0, 0, 0)
    assert robot.__eq__(robot2) == False

def test_emptyEq(robot):
    assert robot.__eq__() == False


