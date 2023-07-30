from flash import Flash
from poligonal_model import PoligonalModel


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash) -> None:
        self.id = id
        self.models = models
        self.flashes = flashes

    def method1(*args):
        pass

    def method2(*args, **kwargs):
        pass
