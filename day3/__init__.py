from functools import reduce
from math import ceil, floor
from types import GeneratorType


def get_rucksacks():
  with open('day3/rucksacks.txt') as f:
    for line in f:
      yield line.strip()


def chunk(values, size):
  '''
  Chunk the values into specific size chunks
  '''
  for i in range(0, len(values), size):
    yield values[i: i + size]


def priority(letter):
  '''
  Get the priority of the letter/character
  '''
  if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
    return ord(letter) - 96
  if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
    return ord(letter) - 38


def shared_char(*args):
  '''
  Get the shared value between all the iterables
  '''
  for ch in args[0]:
    if all(ch in it for it in args[1:]):
      return ch


def part1():
  def result(rucksack):
    midpoint = floor(len(rucksack) / 2)
    return priority(shared_char(rucksack[:midpoint], rucksack[midpoint:]))
  return sum((result(rucksack) for rucksack in get_rucksacks()))


def part2():
  return sum([priority(shared_char(*rucksack)) for rucksack in chunk(list(get_rucksacks()), 3)])


def run():
  print('Day 3')
  print(part1())
  print(part2())
