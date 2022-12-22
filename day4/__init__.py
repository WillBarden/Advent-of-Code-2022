from functools import reduce
from math import ceil, floor
from types import GeneratorType


def get_ranges():
  '''
  Read inputs and parse them into tuples which represent the section ranges
  '''
  with open('day4/input.txt') as f:
    for line in f:
      line = line.strip()
      left, right = line.split(',')
      yield (
        tuple(int(x) for x in left.split('-')), 
        tuple(int(x) for x in right.split('-'))
      )


def completely_overlaps(x, y):
  '''
  Return true if range x completely contains range y
  '''
  return y[0] >= x[0] and y[1] <= x[1]


def partially_overlaps(x, y):
  '''
  Returns true if range x partially overlaps range y
  '''
  return (y[0] >= x[0] and y[0] <= x[1]) or (y[1] >= x[0] and y[1] <= x[1])


def part1():
  return reduce(
    lambda total, range : 
      total + 1 
      if completely_overlaps(range[0], range[1]) or completely_overlaps(range[1], range[0]) 
      else total, 
    get_ranges(), 
    0
  )


def part2():
  return reduce(
    lambda total, range : 
      total + 1 
      if partially_overlaps(range[0], range[1]) or completely_overlaps(range[0], range[1]) or completely_overlaps(range[1], range[0])
      else total, 
    get_ranges(), 
    0
  )


def run():
  print('Day 4')
  print(part1())
  print(part2())
