from abc import ABC, abstractmethod


class WorkInterface(ABC):
    @abstractmethod
    def work(self):
        pass
