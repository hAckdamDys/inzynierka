import uuid
from Util.Directions import Directions

class Robot:
    def __init__(self, x, y, manager, sharedGrid, rotation, algorithm=None):
        self.x = x
        self.y = y
        self.id = uuid.uuid4()
        self.sharedGrid = sharedGrid # how world actually looks
        sharedGrid.addRobot(self)
        self.privateGrid = sharedGrid.getPrivateGridCopy(
            manager)  # how given robot sees world
        self.currentRotation = rotation  # Direction. left, up, right, or down
        self.wantToMove = False # set to True if tries to move
        self.currentAlgorithm = algorithm

    # changes True to 1 and False to -1
    def boolToRotation(self, bool):
        return 2 * bool - 1

    def tryMoveForward(self, inverse=False):
        self.wantToMove = True
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
        self.sharedGrid.moveRobot(self, nextX, nextY)
        # self.privateGrid.moveRobot(self, nextX, nextY)
        self.wantToMove = False

    def tryMoveBackward(self):
        self.tryMoveForward(inverse=True)

    def updatePosition(self, nextX, nextY):
        if self.wantToMove:
            # check if nextX - self.x <= 1
            if abs(nextX-self.x)>1:
                raise ValueError(
                    'Abs value between x and nextX has to be <= 1.')
            if abs(nextY-self.y)>1:
                raise ValueError(
                    'Abs value between y and nextY has to be <= 1.')
            if abs(nextX-self.x) + abs(nextY-self.y) > 1:
                raise ValueError(
                    'Cannot move in x and y direction at once')
            self.x = nextX
            self.y = nextY

    def rotateRight(self, inverse=False):
        rotation = 1
        if inverse:
            rotation=-rotation
        self.currentRotation = Directions(
            (self.currentRotation.value + rotation) % 4)

    def rotateLeft(self):
        self.rotateRight(inverse=True)

    def startWorking(self, algorithm=None):
        if algorithm is not None:
            self.currentAlgorithm = algorithm(self)
        self.currentAlgorithm.startWorking()

    def waitForFinish(self):
        self.currentAlgorithm.waitForFinish()

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
