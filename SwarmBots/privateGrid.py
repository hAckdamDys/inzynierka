from SwarmBots.baseGrid import BaseGrid
import numpy as np


# grid corresponding to robot's view of a map
class PrivateGrid(BaseGrid):
    def __init__(self, width, height, manager, tileGrid=None,
                 tilesFromIndex=None,
                 indexFromTiles=None, lastTileIndex=None) -> None:
        super().__init__(width=width, height=height, manager=manager,
                         tileGrid=tileGrid,
                         tilesFromIndex=tilesFromIndex,
                         indexFromTiles=indexFromTiles,
                         lastTileIndex=lastTileIndex)

