from functools import reduce
from math import ceil, floor
import re
from types import GeneratorType
from copy import deepcopy


def get_forest(fp):
  with open(fp) as f:
    return [[int(ch) for ch in line] for line in [line.strip() for line in f.readlines()]]


def print_forest(forest):
  forest = '\n'.join([''.join([str(tree) for tree in row]) for row in forest])
  print(forest)


def print_visible_trees(visible_trees):
  print_forest([['O' if tree else 'X' for tree in row] for row in visible_trees])


def running_max(values):
  return reduce(
    lambda maxes, value : [value] if len(maxes) == 0 else maxes + [max(maxes[-1], value)], 
    values, 
    []
  )


def invert(matrix):
  matrix_out = deepcopy(matrix)
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      matrix_out[i][j], matrix_out[j][i] = matrix[j][i], matrix[i][j]
  return matrix_out


def left_scan(forest):
  return [running_max(row) for row in forest]


def right_scan(forest):
  return [running_max(row[::-1])[::-1] for row in forest]


def part1():
  forest = get_forest('day8/input.txt')
  visible = [[False for _ in row] for row in forest]

  for i in range(len(forest)):
    max_height = -1
    for j in range(len(forest[i])):
      if forest[i][j] > max_height:
        visible[i][j] = True
        max_height = forest[i][j]

  for i in range(len(forest)):
    max_height = -1
    for j in range(len(forest[i]) - 1, -1, -1):
      if forest[i][j] > max_height:
        visible[i][j] = True
        max_height = forest[i][j]

  for j in range(len(forest[0])):
    max_height = -1
    for i in range(len(forest)):
      if forest[i][j] > max_height:
        visible[i][j] = True
        max_height = forest[i][j]

  for j in range(len(forest[0])):
    max_height = -1
    for i in range(len(forest) -1, -1, -1):
      if forest[i][j] > max_height:
        visible[i][j] = True
        max_height = forest[i][j]

  return sum([sum([1 if tree else 0 for tree in row]) for row in visible])


def part2():
  forest = get_forest('day8/input.txt')
  visible = [[False for _ in row] for row in forest]


def run():
  print('Day 7')
  print(part1())
  print(part2())
