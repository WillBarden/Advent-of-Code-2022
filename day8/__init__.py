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
  lview_forest = left_scan(forest)
  rview_forest = right_scan(forest)
  tview_forest = invert(left_scan(invert(forest)))
  bview_forest = invert(right_scan(invert(forest)))
  visible_trees = [[False] * len(row) for row in forest]
  for i, row in enumerate(forest):
    for j, tree in enumerate(row):
      if i == 0 or i == len(row) - 1:
        visible_trees[i][j] = True
      elif j == 0 or j == len(forest) - 1:
        visible_trees[i][j] = True
      elif lview_forest[i][j - 1] < tree or rview_forest[i][j + 1] < tree or tview_forest[i - 1][j] < tree or bview_forest[i + 1][j] < tree:
        visible_trees[i][j] = True
  return sum([sum([1 if tree else 0 for tree in row]) for row in forest])


def part2():
  pass


def run():
  print('Day 7')
  print(part1())
  print(part2())
