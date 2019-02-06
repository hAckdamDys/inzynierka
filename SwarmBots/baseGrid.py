from SwarmBots.robot import Robot
import numpy as np


# grid corresponding to actual map where robots move and put blocks
class BaseGrid:
    def __init__(self, width, height, tileGrid=None, tilesFromIndex=None,
                 indexFromTiles=None, lastTileIndex=None) -> None:
        self.width = width
        self.height = height
        # grid will have 0 if nothing is on given tile
        # and index of tile otherwise
        if (tileGrid is None) or (tilesFromIndex is None) or \
                (indexFromTiles is None) or (lastTileIndex is None):
            if (tileGrid is not None) or (tilesFromIndex is not None) or \
                    (indexFromTiles is not None) or (
                    lastTileIndex is not None):
                raise ValueError("tileGrid,tilesFromIndex,lastTileIndex and " + \
                                 +"indexFromTiles needs to be all None or all set")
            self.tileGrid = np.zeros((width, height), int)
            self.tilesFromIndex = dict()
            self.indexFromTiles = dict()
            self.lastTileIndex = 0
        else:
            self.tileGrid = tileGrid
            self.tilesFromIndex = tilesFromIndex
            self.indexFromTiles = indexFromTiles
            self.lastTileIndex = lastTileIndex

    def addNewTile(self, tile):
        self.lastTileIndex += 1
        self.tilesFromIndex[self.lastTileIndex] = tile
        self.indexFromTiles[tile] = self.lastTileIndex

    def addTile(self, tile, x, y):
        tileIndex = self.indexFromTiles[tile]
        self.tileGrid[x, y] = tileIndex
