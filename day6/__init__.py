from functools import reduce
from math import ceil, floor
import re
from types import GeneratorType


def get_input():
  with open('day6/input.txt', 'r') as f:
    return f.readline().rstrip()


def add_to_buffer(buffer, value, cap=1):
  buffer.append(value)
  return buffer[-cap:]


def unique(values):
  seen = {}
  for value in values:
    if value in seen.keys():
      return False
    else:
      seen[value] = True
  return True


def part1():
  buffer = []
  for i, ch in enumerate(get_input()):
    buffer = add_to_buffer(buffer, ch, 4)
    if len(buffer) == 4 and unique(buffer):
      return i + 1


def part2():
  pass


def run():
  print('Day 6')
  print(part1())
  print(part2())
