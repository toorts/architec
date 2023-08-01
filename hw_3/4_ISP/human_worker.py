from eat_interface import EatInterface
from work_interface import WorkInterface


class HumanWorker(EatInterface, WorkInterface):
    def work(self) -> None:
        print('Человек работает')

    def eat(self) -> None:
        print('Человек ест')
