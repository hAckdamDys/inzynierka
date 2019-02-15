from Util.directions import Directions
from SwarmBots.robot import Robot
from multiprocessing import Process, Lock


class RobotAlgorithmExecutor():
    def __init__(self, robot):
        self.robot = robot

    def startWorking(self):
        self.process = Process(target=self.startProcess)
        self.process.start()

    def startProcess(self):
        raise ValueError("This method should be overriden")

    def waitForFinish(self):
        self.process.join()
