
import random
import math
import sys

map = {}

size = int(input("Map size: "))
island_size = int(input("Island size: "))

for y in range(size):
  for x in range(size):
    map[x, y] = " "

def build(map, x, y):
  recursive_build(map, x, y, x, y, island_size)

def recursive_build(map, x, y, startX, startY, island_size):
  if x < 0 or y < 0 or x > size - 1 or y > size - 1 or map[x, y] == "X":
    return
  dst = math.sqrt(math.pow(x - startX, 2) + math.pow(y - startY, 2))
  if random.randrange(island_size) < dst:
    return
  map[x, y] = "X"
  recursive_build(map, x + 1, y + 1, startX, startY, island_size)
  recursive_build(map, x    , y + 1, startX, startY, island_size)
  recursive_build(map, x - 1, y + 1, startX, startY, island_size)
  recursive_build(map, x + 1, y    , startX, startY, island_size)
  recursive_build(map, x - 1, y    , startX, startY, island_size)
  recursive_build(map, x + 1, y - 1, startX, startY, island_size)
  recursive_build(map, x    , y - 1, startX, startY, island_size)
  recursive_build(map, x - 1, y - 1, startX, startY, island_size)

def print_map(map):
  for y in range(size):
    for x in range(size):
      print(map[x, y], end="")
      print(map[x, y], end="")
    print()

sys.setrecursionlimit(size * size) # python is bad this should be enough to loop through everything, so long as user wont enter a billion
build(map, int(size / 2), int(size / 2))
print_map(map)
