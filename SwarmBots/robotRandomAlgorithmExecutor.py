from Util.directions import Directions
from SwarmBots.robot import Robot
from SwarmBots.robotAlgorithmExecutor import RobotAlgorithmExecutor
import time
import random


class RobotRandomAlgorithmExecutor(RobotAlgorithmExecutor):
    def __init__(self, robot):
        self.robot = robot

    def startProcess(self):
        iteration = 0
        while True:
            # make random action
            actionNum = random.randint(0, 5)
            if actionNum == 0:
                print(iteration, ': robot=', self.robot, 'rot right')
                self.robot.rotateRight()
            elif actionNum == 1:
                print(iteration, ': robot=', self.robot, 'rot left')
                self.robot.rotateLeft()
            elif actionNum == 2:
                print(iteration, ': robot=', self.robot, 'try forward')
                self.robot.tryMoveForward()
            elif actionNum == 3:
                print(iteration, ': robot=', self.robot, 'try backward')
                self.robot.tryMoveBackward()
            elif actionNum == 4:
                print(iteration, ': robot=', self.robot, 'put tile')
                self.robot.tryPutTile()
            elif actionNum == 5:
                print(iteration, ': robot=', self.robot,
                      'take tile from source')
                self.robot.takeTileFromSource()

            time.sleep(1)
            iteration += 1
            # if (iteration > 5):
            #     return
