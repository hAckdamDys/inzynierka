# import unittest
#
from Robot import Robot
#
#
# class RobotTest(unittest.TestCase):
#     def setUp(self):
#         self.robot = Robot(1,1,1,1,1)
#
#     def test_initialization(self):
#         self.assertTrue(self.robot)
#         self.assertEqual(self.robot.x, 1)
#         self.assertEqual(self.robot.y, 1)
#         self.assertEqual(self.robot.privateGrid, 1)
#         self.assertEqual(self.robot.realGrid, 1)
#         self.assertEqual(self.robot.currentRotation, 1)
#
#     def test_tryMoveForward(self):
#
#
#
# if __name__ == '__main__':
#     unittest.main()

def test_robotInitialization():
    robot = Robot(1,1,1,1,1)
    assert robot

def test_tryMoveForward():
    robot = Robot(1, 1, 1, 1, 1)
