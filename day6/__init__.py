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


def first_unique_chunk(line, unique_chunk_len):
  buffer = []
  for i, ch in enumerate(line):
    buffer = add_to_buffer(buffer, ch, unique_chunk_len)
    if len(buffer) == unique_chunk_len and unique(buffer):
      return i + 1


def part1():
  return first_unique_chunk(get_input(), 4)


def part2():
  return first_unique_chunk(get_input(), 14)


def run():
  print('Day 6')
  print(part1())
  print(part2())
