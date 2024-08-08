"""A class of cube from company A by Farseen Ashraf"""

from interface_cube_a import ICubeA
import time


class CubeA(ICubeA):
    """A hypothetical Cube manufacturer for company A which implements ICubeA"""
    # a static variable indicating the last time the cube the manufactured
    last_time = int(time.time())

    def __init__(self):
        self.height = self.width = self.depth = 0

    def manufacture(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        # if not busy then manufacture a cube with dimensions
        now = int(time.time())
        if now > int(CubeA.last_time + 1):
            CubeA.last_time = now
            return True
        return False  # busy
