from abc import ABC, abstractmethod


class IEating(ABC):
    @abstractmethod
    def eat(self):
        pass
