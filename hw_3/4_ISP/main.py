from human_worker import HumanWorker
from robot_worker import RobotWorker

if __name__ == '__main__':
    human_worker = HumanWorker()
    human_worker.work()
    human_worker.eat()

    robot_worker = RobotWorker()
    robot_worker.work()
