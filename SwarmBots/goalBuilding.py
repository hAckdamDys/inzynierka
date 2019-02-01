import numpy as np
import os


# static grid where there are only goal
class GoalBuilding:
    def __init__(self, textGrid):
        self.parseTextGrid(textGrid)

    def parseTextGrid(self, textGrid):
        rowSep = ';'
        textGridTmp = textGrid.replace(os.linesep, rowSep)
        textGridTmp = textGridTmp.replace('\n', rowSep)
        textGridTmp = textGridTmp.lstrip(rowSep).rstrip(rowSep)
        self.height = textGridTmp.count(rowSep)
        firstRow = np.fromstring(textGridTmp.split(rowSep)[0], dtype=int,
                                 sep=' ')
        self.width = firstRow.shape[0]
        self.grid = np.fromstring(textGrid, dtype=int, sep=' ').reshape(
            self.height, self.width)
