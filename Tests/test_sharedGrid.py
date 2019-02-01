import pytest
from SwarmBots.sharedGrid import SharedGrid

def test_sharedGridInitialization():
    sharedGrid = SharedGrid(8, 8)
    assert sharedGrid
