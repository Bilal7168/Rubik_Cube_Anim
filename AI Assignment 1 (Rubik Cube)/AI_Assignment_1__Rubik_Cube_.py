
from Rubik_Cube import Rubik_Cube

import sys

import copy

from Intializer_funcs import *

sys.setrecursionlimit(500000)

R_c = Rubik_Cube()

print(sys.getrecursionlimit())
R_c.print_all_faces()

Rubik_Cube_Anim(R_c)


