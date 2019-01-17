from Robot import Robot
import numpy as np


# grid corresponding to actual map where robots move and put blocks
class BuildingGrid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        # grid will have 0 if nothing is on given tile
        # and index of tile otherwise
        self.tileGrid = np.zeros((width,height),int)
        self.tilesFromIndex = dict()
        self.indexFromTiles = dict()
        self.lastTileIndex = 0
        # robots are on separate layer on grid to simplify things
        # since robots are unique we dont need indexes
        self.robotsGrid = np.zeros((width,height), dtype=Robot)
        self.positionFromRobot = dict()

    def addNewTile(self, tile):
        self.lastTileIndex += 1
        self.tilesFromIndex[self.lastTileIndex] = tile
        self.indexFromTiles[tile] = self.lastTileIndex

    def addTile(self, tile, x, y):
        tileIndex=self.indexFromTiles[tile]
        self.tileGrid[x,y]=tileIndex

    def addRobot(self, robot):
        self.robotsGrid[robot.x,robot.y] = robot
        self.positionFromRobot[robot] = (robot.x,robot.y)

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
        robot.updatePosition(nextX,nextY)
