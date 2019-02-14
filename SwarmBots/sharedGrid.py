from SwarmBots.baseGrid import BaseGrid
from SwarmBots.robot import Robot
import numpy as np
from multiprocessing import Manager
from privateGrid import PrivateGrid


class SharedGrid(BaseGrid):
    noRobot = 0

    def __init__(self, width, height, manager) -> None:
        super().__init__(width=width, height=height, manager=manager)
        # robots are on separate layer on grid to simplify things
        # since robots are unique we dont need indexes
        self.robotsGrid = np.zeros((self.width, self.height), dtype=Robot)
        self.positionFromRobot = manager.dict()

    def getPrivateGridCopy(self, manager) -> PrivateGrid:
        privateGrid = PrivateGrid(width=self.width, height=self.height,
                                  manager=manager,
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
        canMove = self.checkIfCanMove(robot, nextX, nextY)
        if not canMove:
            return
        # clean last position
        self.robotsGrid[robot.x, robot.y] = 0
        # update new position
        self.robotsGrid[nextX, nextY] = robot
        self.positionFromRobot[robot] = (nextX, nextY)
        robot.updatePosition(nextX, nextY)

    def checkIfCanMove(self, robot, nextX, nextY):
        # can't move out of grid
        if (nextX < 0) or (nextY < 0):
            print("out of bound", nextX, nextY)
            return False
        if (nextX >= self.width) or (nextY >= self.width):
            print("out of bound", nextX, nextY)
            return False
        # TODO maybe instead of bool return some information so robot knows what it hit
        if self.robotsGrid[nextX, nextY] != 0:
            print("there is a robot on ", self.robotsGrid[nextX, nextY])
            return False
        if self.tileGrid[nextY, nextY] != 0:
            # TODO same here if robot can enter for example ramp then True
            # something like "if robot can enter tile from his position then true"
            print("there is some tile on ", self.robotsGrid[nextX, nextY])
            return False
        return True
