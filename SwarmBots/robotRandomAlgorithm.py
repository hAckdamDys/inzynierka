from Util.Directions import Directions
from SwarmBots.robot import Robot
from SwarmBots.robotAlgorithm import RobotAlgorithm
import time


class RobotRandomAlgorithm(RobotAlgorithm):
    def __init__(self, robot):
        self.robot = robot

    def startProcess(self):
        iteration = 0
        while True:
            print(iteration, ': robot=', self.robot)
            time.sleep(1)
            iteration += 1
            if (iteration > 5):
                return
