"""A class of cube from company B by Farseen Ashraf"""

from interface_cube_b import ICubeB
import time


class CubeB(ICubeB):
    """A hypothetical Cube manufacturer for company B which implements ICubeB"""
    last_time = int(time.time())

    def create(self, top_left_front, bottom_right_back):
        now = int(time.time())
        if now > int(CubeB.last_time+2):
            CubeB.last_time = now
            return True
        return False  # busy
