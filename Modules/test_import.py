# import main

# # print(main.x)
# print(main.add(10,20))
# print(main.subtract(40,20))

from main import add, subtract

print(add(10,20))
print(subtract(40,5))

# from main import add as sum, subtract as sub

# print(sum(10,20))
# print(sub(30,10))

import time
from importlib import reload
import module1

time.sleep(5)
reload(module1)