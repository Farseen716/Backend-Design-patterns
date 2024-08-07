"""Adapter Example use case"""

import random
import time
from cube_a import CubeA
from cube_b_adapter import CubeBAdapter

total_cubes = 5
counter = 0
while counter < total_cubes:
    # manufacture 5 cubes from which ever supplier can manufacture it first
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    depth = random.randint(1, 10)
    cube = CubeA()
    success = cube.manufacture(height=height, depth=depth, width=width)
    if success:
        print(f"Company A is building Cube id: {id(cube)}, "
              f"{cube.width}x{cube.height}x{cube.depth}")
        counter+=1
    else:    # try another manufacturer
        print("Company A is busy, trying Company B")
        cube = CubeBAdapter()
        success  = cube.manufacture(height=height, width=width, depth=depth)
        if success:
            print(f"Company B is building Cube id: {id(cube)}, "
                  f"{cube.width}x{cube.height}x{cube.depth}")
            counter += 1
        else:
            print("Company B is busy, trying Company A")
    # Wait for some time before manufacturing a new cube
    time.sleep(1)
print(f"{total_cubes} cubes have been manufactured")
