from functools import reduce
from math import ceil, floor
import re
from types import GeneratorType


def get_input():
  '''
  Get input lines as a generator
  '''
  f = open('day5/input.txt', 'r')
  
  # Parse crates
  crates = [[] for _ in range(9)]
  line = f.readline().rstrip()
  while len(line) == 35:
    crate_values = [line[i] for i in list(range(1, 35, 4))]
    for i, value in enumerate(crate_values):
      if value != ' ':
        crates[i].insert(0, value)
    line = f.readline().rstrip()

  # Move through space
  f.readline()

  # Parse moves
  moves = []
  line = f.readline().rstrip()
  while line:
    res = re.findall('^move (\d+) from (\d+) to (\d+)$', line)
    res = tuple(int(r) for r in res[0])
    res = (res[0], res[1] - 1, res[2] - 1)
    moves.append(res)
    line = f.readline().rstrip()

  f.close()
  return (crates, moves)


def move_crate(crates, src, dst, moves=1):
  for _ in range(moves):
    crate = crates[src].pop()
    crates[dst].append(crate)
  return crates


def move_crates(crates, src, dst, count=1):
  moving_crates = crates[src][-count:]
  crates[src] = crates[src][:-count]
  crates[dst] += moving_crates
  return crates


def last(values):
  return values[len(values) - 1]


def part1():
  crates, moves = get_input()
  crates = reduce(
    lambda crates, move : move_crate(crates, move[1], move[2], move[0]),
    moves,
    crates
  )
  return ''.join([last(crate) for crate in crates])
  

def part2():
  crates, moves = get_input()
  crates = reduce(
    lambda crates, move : move_crates(crates, move[1], move[2], move[0]),
    moves,
    crates
  )
  return ''.join([last(crate) for crate in crates])


def run():
  print('Day 5')
  print(part1())
  print(part2())
