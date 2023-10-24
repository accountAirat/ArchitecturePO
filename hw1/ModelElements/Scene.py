from typing import List

import PoligonalModel
import Flash
import Camera


class Scene:
    id: int

    def __init__(self, models: List[PoligonalModel], cameras: List[Flash], flashes: List[Camera] = [], ):
        if len(models) == 0:
            raise Exception('Список models пуст')
        self.models = models

        if len(cameras) == 0:
            raise Exception('Список cameras пуст')
        self.cameras = cameras

        self.flashes = flashes

    def method1(self, item):
        ...
        return item

    def method2(self, first_item, second_item):
        ...
        return first_item
