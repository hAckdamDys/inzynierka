from SwarmBots.baseGrid import BaseGrid
from SwarmBots.robot import Robot
import numpy as np
from multiprocessing import Manager
from privateGrid import PrivateGrid
from SwarmBots.Util.hitInformation import HitInformation
from multiprocessing import Lock


class SharedGrid(BaseGrid):
    noRobot = 0

    def __init__(self, width, height, manager) -> None:
        super().__init__(width=width, height=height, manager=manager)
        # robots are on separate layer on grid to simplify things
        # since robots are unique we dont need indexes
        # self.lock = Lock()
        # self.lock = manager.Lock()
        self.robotsGrid = manager.list()
        self.robotsGrid.append(
            np.zeros((self.width, self.height), dtype=Robot))
        self.positionFromRobot = manager.dict()

    def getPrivateGridCopy(self, manager) -> PrivateGrid:
        privateGrid = PrivateGrid(width=self.width, height=self.height,
                                  manager=manager,
                                  tileGrid=self.tileGrid,
                                  tilesFromIndex=self.tilesFromIndex,
                                  indexFromTiles=self.indexFromTiles,
                                  lastTileIndex=self.lastTileIndex)
        return privateGrid

    def setRobotsGridElement(self, x, y, robot):
        # print("setting robot on ",x,y)
        self.lock.acquire()
        a = self.robotsGrid[0]
        a[x, y] = robot
        self.robotsGrid[0] = a
        self.lock.release()
        # print(self.robotsGrid)

    def getRobotsGridElement(self, x, y):
        return self.robotsGrid[0][x, y]

    def addRobot(self, robot):
        if self.getRobotsGridElement(robot.x, robot.y) != SharedGrid.noRobot:
            raise ValueError("Cannot add robot on top of another one")
        self.setRobotsGridElement(robot.x, robot.y, robot)
        self.positionFromRobot[robot] = (robot.x, robot.y)

    def getGridHitInformation(self, nextX, nextY) -> HitInformation:
        # can't move out of grid
        if (nextX < 0) or (nextY < 0):
            print("out of bound", nextX, nextY)
            return HitInformation.OUTOFBOUND
        if (nextX >= self.width) or (nextY >= self.height):
            print("out of bound", nextX, nextY)
            return HitInformation.OUTOFBOUND
        tmp = self.getRobotsGridElement(nextX, nextY)
        if tmp != 0:
            print("there is a robot on ", tmp)
            return HitInformation.ROBOT
        if self.getTileIndex(nextX, nextY) != 0:
            # print("there is some tile on ", self.robotsGrid[nextX, nextY])
            return HitInformation.TILE
        return HitInformation.NOHIT

    def moveRobot(self, robot, nextX, nextY):
        hitInformation = self.getGridHitInformation(nextX, nextY)
        if hitInformation != HitInformation.NOHIT:
            return hitInformation
        # clean last position
        self.setRobotsGridElement(robot.x, robot.y, 0)
        # update new position
        self.setRobotsGridElement(nextX, nextY, robot)
        self.positionFromRobot[robot] = (nextX, nextY)
        robot.updatePosition(nextX, nextY)
        return hitInformation

    def putTile(self, x, y):
        hitInformation = self.getGridHitInformation(x, y)
        if hitInformation == HitInformation.NOHIT:
            self.addTile(hitInformation.TILE, x, y)
        return hitInformation

    def robotToR(self, x):
        # print("?",type(x))
        if type(x).__name__ == "Robot":
            return 1
        return 0

    def __str__(self):
        return super().__str__() + "\nrobot grid:\n" + \
               str(np.vectorize(self.robotToR)(self.robotsGrid[0].T))
