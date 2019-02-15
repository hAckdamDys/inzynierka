from goalBuilding import GoalBuilding
from robot import Robot
from sharedGrid import SharedGrid
from Util.directions import Directions
from SwarmBots.robotRandomAlgorithmExecutor import RobotRandomAlgorithmExecutor
from SwarmBots.robot1Executor import Robot1Executor
from SwarmBots.robot2Executor import Robot2Executor
from multiprocessing import Manager


def main():
    manager = Manager()
    goalBuilding = GoalBuilding("""
        0 0 0 0 0 0
        1 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        """)
    sharedGrid = SharedGrid(width=goalBuilding.width,
                            height=goalBuilding.height, manager=manager)
    robot1 = Robot(0, 0, manager, sharedGrid, Directions.LEFT)
    robot2 = Robot(5, 4, manager, sharedGrid, Directions.RIGHT)
    robot1Executor = RobotRandomAlgorithmExecutor(robot1)
    robot2Executor = RobotRandomAlgorithmExecutor(robot2)
    # robot1Executor = Robot1Executor(robot1)
    # robot2Executor = Robot2Executor([robot2, robot1])
    robot1Executor.startWorking()
    robot2Executor.startWorking()
    robot1Executor.waitForFinish()
    robot2Executor.waitForFinish()

    # print("step", robot, robot2)
    # robot.tryMoveForward()
    # robot2.tryMoveForward()
    # print("step", robot, robot2)
    # robot.rotateRight()
    # robot2.rotateRight()
    # print("step", robot, robot2)
    # robot.tryMoveForward()
    # robot2.tryMoveForward()
    # print("step", robot, robot2)
    # robot.tryMoveForward()
    # robot2.tryMoveForward()
    # print("step", robot, robot2)


import threading
import time
import numpy as np
import random

loopNum = 100000


def worker(num):
    """thread worker function"""
    r = 1
    for i in range(loopNum):
        if i % (loopNum // 10) == 0:
            print('Worker: %s, iter: %s' % (num, i))
            time.sleep(0.1)
        r = np.log(i / (np.log(10 * r) + random.randint(1, 2))) + r // 3


from multiprocessing import Process, Lock


def f(l, num):
    r = 1
    for i in range(loopNum):
        if i % (loopNum // 10) == 0:
            l.acquire()
            print('Worker: %s, iter: %s' % (num, i))
            l.release()
            time.sleep(0.1)
        r = np.log((i + random.randint(3, 66)) / random.randint(1, 2)) + r // 3


def f2(l, num, mlist):
    l.acquire()
    print(num, ":", len(mlist))
    mlist.append(num)
    l.release()
    time.sleep(3)
    l.acquire()
    print(num, ":", mlist)
    l.release()

def main_multiprocessing():
    lock = Lock()
    processes = []
    manager = Manager()
    managerlist = manager.list()
    for num in range(5):
        # robot = Robot(2, 2, manager, sharedGrid=SharedGrid(3, 3, manager),
        #               rotation=Directions.RIGHT)
        p = Process(target=f2, args=(lock, num, managerlist))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def main_threading():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

if __name__ == '__main__':
    main()