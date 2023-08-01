from work_interface import WorkInterface


class RobotWorker(WorkInterface):
    def work(self) -> None:
        print('Робот работает')
