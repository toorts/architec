from model_elements.poligonal_model import PoligonalModel
from model_elements.scene import Scene
from model_elements.camera import Camera
from model_elements.flash import Flash

from i_model_changed_observer import IModelChangedObserver
from i_model_changer import IModelChanger


class ModelStore(IModelChanger):
    def __init__(self,
                 models: PoligonalModel,
                 scenes: Scene,
                 flashes: Flash,
                 cameras: Camera,
                 changedObservers: IModelChangedObserver) -> None:
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__changedObservers = changedObservers

    def get_scena(data: int) -> Scene:
        return data

    def notify_change(data: IModelChanger) -> None:
        pass
