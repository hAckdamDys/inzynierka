import pytest
from SwarmBots.SharedGrid import SharedGrid

def test_sharedGridInitialization():
    sharedGrid = SharedGrid(8, 8)
    assert sharedGrid
