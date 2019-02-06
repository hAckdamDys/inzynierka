from SwarmBots.baseGrid import BaseGrid
from SwarmBots.robot import Robot
import numpy as np

from privateGrid import PrivateGrid


class SharedGrid(BaseGrid):
    noRobot = 0

    def __init__(self, width, height) -> None:
        super().__init__(width=width, height=height)
        # robots are on separate layer on grid to simplify things
        # since robots are unique we dont need indexes
        self.robotsGrid = np.zeros((self.width, self.height), dtype=Robot)
        self.positionFromRobot = dict()

    def getPrivateGridCopy(self) -> PrivateGrid:
        privateGrid = PrivateGrid(width=self.width, height=self.height,
                                  tileGrid=self.tileGrid.copy(),
                                  tilesFromIndex=self.tilesFromIndex.copy(),
                                  indexFromTiles=self.indexFromTiles.copy(),
                                  lastTileIndex=self.lastTileIndex)
        return privateGrid

    def addRobot(self, robot):
        if self.robotsGrid[robot.x, robot.y] != SharedGrid.noRobot:
            raise ValueError("Cannot add robot on top of another one")
        self.robotsGrid[robot.x, robot.y] = robot
        self.positionFromRobot[robot] = (robot.x, robot.y)

    def moveRobot(self, robot, nextX, nextY):
        # TODO: implement this function
        canMove = self.checkIfCanMove(robot)
        if not canMove:
            return
        # clean last position
        self.robotsGrid[robot.x, robot.y] = 0
        # update new position
        self.robotsGrid[nextX, nextY] = robot
        self.positionFromRobot[robot] = (nextX, nextY)
        robot.updatePosition(nextX, nextY)
