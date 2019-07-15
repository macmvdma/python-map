
import random
import math
import sys

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

def new_map(size):
  map = {}
  for y in range(size):
    for x in range(size):
      map[x, y] = " "
  return map

def print_usage():
  print("Usage:  python map.py size [island_size]")
  print("")
  print("size:\t\tthe width and height of the map")
  print("island_size:\tthe average size of the island, and will default to half of size")

def get_args():
  args = sys.argv
  args.pop(0)
  if len(args) < 1:
    print_usage()
    exit()
  elif len(args) < 2:
    return (int(args[0]), int(int(args[0]) / 2))
  elif len(args) < 3:
    return (int(args[0]), int(args[1]))
  else:
    print_usage()
    exit()

size, island_size = get_args()

sys.setrecursionlimit(size * size) # python is bad this should be enough to loop through everything, so long as user doesn't enter a billion
map = new_map(size)
build(map, int(size / 2), int(size / 2))
print_map(map)
