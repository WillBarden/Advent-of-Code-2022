from functools import reduce
from math import ceil, floor

def get_rucksacks():
  with open('day3/rucksacks.txt') as f:
    for line in f:
      yield line.strip()


def priority(letter):
  '''
  Get the priority of the letter/character
  '''
  if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
    return ord(letter) - 96
  if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
    return ord(letter) - 38


def shared_char(left, right):
  '''
  Get the shared value between the two iterables
  '''
  for ch in left:
    if ch in right:
      return ch


def part1():
  def result(rucksack):
    midpoint = floor(len(rucksack) / 2)
    return priority(shared_char(rucksack[:midpoint], rucksack[midpoint:]))
  return sum((result(rucksack) for rucksack in get_rucksacks()))


def run():
  print('Day 3')
  print(part1())
