import uuid
from Util.directions import Directions
from SwarmBots.Util.hitInformation import HitInformation


class Robot:
    def __init__(self, x, y, manager, sharedGrid, rotation, algorithm=None):
        self.x = x
        self.y = y
        self.id = uuid.uuid4()
        self.sharedGrid = sharedGrid  # how world actually looks
        sharedGrid.addRobot(self)
        self.privateGrid = sharedGrid.getPrivateGridCopy(
            manager)  # how given robot sees world
        self.currentRotation = rotation  # Direction. left, up, right, or down
        self.wantToMove = False  # set to True if tries to move
        self.currentAlgorithm = algorithm
        self.hasTile = False

    # changes True to 1 and False to -1
    def boolToRotation(self, bool):
        return 2 * bool - 1

    def takeTileFromSource(self):
        self.hasTile = True

    def takeTile(self):
        pass
        # 1. check if tile exist
        # 2. if exist then take actualize private and shared grid

    def getNextXY(self, inverse=False):
        # if left or right then x axis
        isXAxis = (self.currentRotation.value % 2 == 0)
        # if right or down we add to x or y
        movement = (self.currentRotation.value >= 2)
        if inverse:
            movement = (not movement)
        nextX = self.x
        nextY = self.y
        if isXAxis:
            nextX += self.boolToRotation(movement)
        else:
            nextY += self.boolToRotation(movement)
        return nextX, nextY

    def privateGridUpdateHitInformation(self, hitInformation, nextX, nextY):
        if hitInformation != HitInformation.NOHIT:
            # actualize private grid with that information
            if hitInformation == HitInformation.TILE:
                self.privateGrid.addTile(hitInformation, nextX, nextY)

    def tryPutTile(self):
        if not self.hasTile:
            return False  # or raise error?
        nextX, nextY = self.getNextXY()
        hitInformation = self.sharedGrid.putTile(nextX, nextY)
        self.privateGridUpdateHitInformation(hitInformation, nextX, nextY)
        if hitInformation == HitInformation.NOHIT:
            self.hasTile = False
        return hitInformation

    def tryMoveForward(self, inverse=False):
        self.wantToMove = True
        nextX, nextY = self.getNextXY(inverse=inverse)
        hitInformation = self.sharedGrid.moveRobot(self, nextX, nextY)
        self.privateGridUpdateHitInformation(hitInformation, nextX, nextY)
        self.wantToMove = False
        return hitInformation  # so algorithm can know what to do

    def tryMoveBackward(self):
        self.tryMoveForward(inverse=True)

    def updatePosition(self, nextX, nextY):
        if self.wantToMove:
            # check if nextX - self.x <= 1
            if abs(nextX - self.x) > 1:
                raise ValueError(
                    'Abs value between x and nextX has to be <= 1.')
            if abs(nextY - self.y) > 1:
                raise ValueError(
                    'Abs value between y and nextY has to be <= 1.')
            if abs(nextX - self.x) + abs(nextY - self.y) > 1:
                raise ValueError(
                    'Cannot move in x and y direction at once')
            self.x = nextX
            self.y = nextY

    def rotateRight(self, inverse=False):
        rotation = 1
        if inverse:
            rotation = -rotation
        self.currentRotation = Directions(
            (self.currentRotation.value + rotation) % 4)

    def rotateLeft(self):
        self.rotateRight(inverse=True)

    def stopWorking(self):
        if self.currentAlgorithm is None:
            raise ValueError('cannot stop working without algorithm')
        self.currentAlgorithm.stopWorking()

    def __str__(self):
        return str(self.x) + "," + str(self.y)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other=None):
        if other is None:
            return False
        if not isinstance(other, Robot):
            return False
        return self.id == other.id
