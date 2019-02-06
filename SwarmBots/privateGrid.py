from SwarmBots.baseGrid import BaseGrid
import numpy as np


# grid corresponding to actual map where robots move and put blocks
class PrivateGrid(BaseGrid):
    def __init__(self, width, height) -> None:
        super().__init__(width=width, height=height)
