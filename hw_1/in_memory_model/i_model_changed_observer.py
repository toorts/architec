from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass
