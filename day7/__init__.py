from functools import reduce
from math import ceil, floor
import re
from types import GeneratorType


FILE = 'FILE'
DIR = 'DIR'
CMD = 'CMD'


def get_lines():
  with open('day7/input.txt', 'r') as f:
    for line in f.readlines():
      yield line.rstrip()


def parse_file(line):
  m = re.findall('^(\d+)\s(\S+)$', line)
  return (FILE, m[0][0], m[0][1]) if m else None


def parse_dir(line):
  m = re.findall('^dir\s(\S+)$', line)
  return (DIR, m[0]) if m else None


def parse_cmd(line):
  m = re.findall('^\$\s(.+)$', line)
  return (CMD, m[0].split(' ')) if m else None


def parse_line(line):
  for parser in [parse_file, parse_dir, parse_cmd]:
    value = parser(line)
    if value:
      return value


def build_fs(fs, line):
  if line[0] == FILE:
    pass
  elif line[1] == DIR:
    pass
  elif line[2] == CMD:
    pass
  return fs


def part1():
  for line in get_lines():
    print(parse_line(line))


def part2():
  pass


def run():
  print('Day 7')
  print(part1())
  print(part2())
