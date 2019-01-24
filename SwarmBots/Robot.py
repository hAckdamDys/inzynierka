class Robot:
    def __init__(self, x, y, privateGrid, sharedGrid, rotation):
        self.x = x
        self.y = y
        self.privateGrid = privateGrid # how given robot sees world
        self.sharedGrid = sharedGrid # how world actually looks
        self.currentRotation = rotation # left, up, right, down or 0,1,2,3
        self.wantToMove = False # set to True if tries to move

    def tryMoveForward(self, inverse=False):
        self.wantToMove = True
        # if left or right then x axis
        isXAxis = (self.currentRotation % 2 == 0)
        # if right or down we add to x or y
        movement = (self.currentRotation >= 2)
        if inverse:
            movement = (not movement)
        nextX = self.x
        nextY = self.y
        if isXAxis:
            nextX+=movement
        else:
            nextY+=movement
        self.sharedGrid.moveRobot(self, nextX, nextY)
        self.privateGrid.moveRobot(self, nextX, nextY)
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
        self.currentRotation = (self.currentRotation+rotation)%4

    def rotateLeft(self):
        self.rotateRight(inverse=True)