from SwarmBots.robot import Robot
import numpy as np


# grid corresponding to actual map where robots move and put blocks
class BaseGrid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        # grid will have 0 if nothing is on given tile
        # and index of tile otherwise
        self.tileGrid = np.zeros((width, height), int)
        self.tilesFromIndex = dict()
        self.indexFromTiles = dict()
        self.lastTileIndex = 0

    def addNewTile(self, tile):
        self.lastTileIndex += 1
        self.tilesFromIndex[self.lastTileIndex] = tile
        self.indexFromTiles[tile] = self.lastTileIndex

    def addTile(self, tile, x, y):
        tileIndex = self.indexFromTiles[tile]
        self.tileGrid[x, y] = tileIndex
