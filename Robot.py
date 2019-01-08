class Robot:
    def __init__(self, x, y, privateGrid, realGrid, rotation):
        self.x = x
        self.y = y
        self.privateGrid = privateGrid
        self.realGrid = realGrid
        self.currentRotation = rotation # left, up, right, down or 0,1,2,3

    def tryMoveForward(self, inverse=False):
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
        self.realGrid.moveRobot(self, nextX, nextY)
        self.privateGrid.moveRobot(self, nextX, nextY)

    def tryMoveBackward(self):
        self.moveForward(inverse=True)

    def updatePosition(self, nextX, nextY):
        self.x = nextX
        self.y = nextY

    def rotateRight(self, inverse=False):
        rotation = 1
        if inverse:
            rotation=-rotation
        self.rotation = (self.rotation+rotation)%4

    def rotateLeft(self):
        self.rotateRight(inverse=True)