from enum import Enum


class HitInformation(Enum):
    OUTOFBOUND = 0
    ROBOT = 1
    TILE = 2
    NOHIT = 3
