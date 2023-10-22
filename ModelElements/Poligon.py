from typing import List
from Stuff import Point3D
import Texture


class Poligon:
    points: list

    def __int__(self, points: List[Point3D] = []):
        self.points = points
