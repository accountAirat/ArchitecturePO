from typing import List

import IModelChanger, IModelChangedObserver
from ModelElements import PoligonalModel, Scene, Flash, Camera


class ModelStore(IModelChanger):
    def __init__(self, change_observers: List[IModelChangedObserver]):
        self.change_observers = change_observers
        self.models: List[PoligonalModel] = [PoligonalModel(None)]
        self.flashes: List[Flash] = [Flash()]
        self.cameras: List[Camera] = [Camera()]
        self.scenes: List[Scene] = [Scene(self.models, self.cameras, self.flashes)]
        self.__change_observers = change_observers

    def get_scene(self, number: int) -> Scene:
        pass

    def notify_change(self, sender: IModelChanger) -> None:
        pass
