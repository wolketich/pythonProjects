# Modules, examples of using

import math
print(math.sqrt(16)) # -> 4

# Import specific functions from a module
from math import ceil, floor 
print(ceil(3.7))   # -> 4
print(floor(3.7))  # -> 3

# Import all functions from a module
from math import * 

# Import module with an alias name

import math as mate
print(mate.sqr(4)) # -> 16
