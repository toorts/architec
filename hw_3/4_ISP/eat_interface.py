from abc import ABC, abstractmethod


class EatInterface(ABC):
    @abstractmethod
    def eat(self):
        pass
