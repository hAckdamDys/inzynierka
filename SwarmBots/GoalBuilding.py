import numpy as np
import os


# static grid where there are only goal
class GoalBuilding:
    def __init__(self, textGrid):
        self.parseTextGrid(textGrid)

    def parseTextGrid(self, textGrid):
        textGrid=";".join([s.lstrip(' ').rstrip(' ') for s in textGrid.splitlines() if s]).lstrip(';').rstrip(';')
        textGrid=' '.join(textGrid.split())
        textGrid=textGrid.replace(' ',',')
        self.grid=np.array(np.matrix(textGrid))
        self.height=self.grid.shape[0]
        self.width=self.grid.shape[1]

## TODO: add test to check for example this:
# exampleTextGrid="""
# 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0
# 0 0 1 2 1 0 0
# 0 1 2 3 2 1 0
# 0 0 1 2 1 0 0
# 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0
# """

# to this:
# np.array([[0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 1, 0, 0, 0],
#        [0, 0, 1, 2, 1, 0, 0],
#        [0, 1, 2, 3, 2, 1, 0],
#        [0, 0, 1, 2, 1, 0, 0],
#        [0, 0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0]])

# and maybe some others
