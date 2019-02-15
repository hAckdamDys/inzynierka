from SwarmBots.robot import Robot
import numpy as np
from multiprocessing import Manager
from SwarmBots.Util.hitInformation import HitInformation

# grid corresponding to actual map where robots move and put blocks
class BaseGrid:
    def __init__(self, width, height, manager, tileGrid=None,
                 tilesFromIndex=None,
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
                raise ValueError("tileGrid,tilesFromIndex,lastTileIndex and " +
                                 "indexFromTiles needs to be all None or all set")
            self.tileGrid = manager.list()
            self.tileGrid.append(np.zeros((width, height), int))
            self.tilesFromIndex = manager.dict()
            self.indexFromTiles = manager.dict()
            self.lastTileIndex = 0
            for hitInformation in HitInformation:
                self.addNewTile(hitInformation)
        else:
            self.tileGrid = manager.list()
            self.tileGrid.append(tileGrid[0].copy())
            self.tilesFromIndex = tilesFromIndex.copy()
            self.indexFromTiles = indexFromTiles.copy()
            self.lastTileIndex = lastTileIndex

    def addNewTile(self, tile):
        self.lastTileIndex += 1
        self.tilesFromIndex[self.lastTileIndex] = tile
        self.indexFromTiles[tile] = self.lastTileIndex

    def getTileIndex(self, x, y):
        return self.tileGrid[0][x, y]

    def addTile(self, tile, x, y):
        tileIndex = self.indexFromTiles[tile]
        a = self.tileGrid[0]
        a[x, y] = tileIndex
        self.tileGrid[0] = a
        print("XY", self)

    def __str__(self):
        print(hash(self))
        print(type(self))
        return "tiles:\n" + str(self.tileGrid[0].T)
