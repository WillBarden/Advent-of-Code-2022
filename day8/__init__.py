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


def scenic_score(forest, i, j):
  HEIGHT = len(forest[0])
  WIDTH = len(forest[1])
  height = forest[i][j]

  # To the left
  dist = 0
  if j - 1 > 0:
    for k in range(j - 1, -1, -1):
      if forest[i][k] < height:
        dist += 1
      else:
        break
  score = dist

  # To the right
  dist = 0
  if j + 1 < WIDTH:
    for k in range(j + 1, WIDTH):
      if forest[i][k] < height:
        dist += 1
      else:
        break
  score *= dist

  # To the top
  dist = 0
  if i - 1 > 0:
    for k in range(i - 1, -1, -1):
      if forest[k][j] < height:
        dist += 1
      else:
        break
  score *= dist

  # To the bottom
  dist = 0
  if i + 1 < HEIGHT:
    for k in range(i + 1, HEIGHT):
      if forest[k][j] < height:
        dist += 1
      else:
        break
    score *= dist
  return score


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
  scores = [[0 for _ in row] for row in forest]
  for i in range(len(forest)):
    for j in range(len(forest[i])):
      scores[i][j] = scenic_score(forest, i, j)
  return max([max(row) for row in scores])


def run():
  print('Day 7')
  print(part1())
  print(part2())
