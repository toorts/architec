from abc import ABC, abstractmethod


class IWorking(ABC):
    @abstractmethod
    def work(self):
        pass
