import functools, sys, os

from utils import sort, lcap, rcap

def get_test_data():
  batch = []
  with open('day1/calories.txt', 'r') as f:
    for line in (line.strip() for line in f.readlines()):
      if len(line) == 0:
        yield batch
        batch = []
      else:
        batch.append(int(line))

def top_calories():
  return functools.reduce(lambda agg, val : max(sum(val), agg), get_test_data(), 0)

def top3_calories():
  return sum(functools.reduce(lambda agg, val : lcap(sort([sum(val), *agg]), 3), get_test_data(), []))

def run():
  print('Day 1')
  print(top_calories())
  print(top3_calories())
