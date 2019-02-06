from goalBuilding import GoalBuilding
from robot import Robot
from sharedGrid import SharedGrid
from Util.Directions import Directions


def main():
    goalBuilding = GoalBuilding("""
        0 0 0
        1 0 0
        0 0 0
        """)
    sharedGrid = SharedGrid(width=goalBuilding.width,
                            height=goalBuilding.height)
    robot = Robot(2, 2, sharedGrid, Directions.LEFT)
    robot2 = Robot(0, 0, sharedGrid, Directions.RIGHT)
    print("step", robot, robot2)
    robot.tryMoveForward()
    robot2.tryMoveForward()
    print("step", robot, robot2)
    robot.rotateRight()
    robot2.rotateRight()
    print("step", robot, robot2)
    robot.tryMoveForward()
    robot2.tryMoveForward()
    print("step", robot, robot2)
    robot.tryMoveForward()
    robot2.tryMoveForward()
    print("step", robot, robot2)

if __name__ == '__main__':
    main()