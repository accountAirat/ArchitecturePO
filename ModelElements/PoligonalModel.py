from typing import List

from Stuff import Point3D
import Texture
import Poligon


class PoligonalModel:
    def __int__(self, textures: List[Texture]):
        self.poligons: List[Poligon] = [Poligon([Point3D()])]
        self.textures: List[Texture] = textures
