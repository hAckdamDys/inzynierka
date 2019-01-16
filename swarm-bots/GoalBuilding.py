import numpy as np

# static grid where there are only goal
class GoalBuilding:
    def __init__(self, width, height, textGrid):
        self.width=width
        self.height=height
        self.grid=np.fromstring(textGrid,dtype=int,sep=' ').reshape(width,height)


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