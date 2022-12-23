from functools import reduce
from math import ceil, floor
import re
from types import GeneratorType


FILE = 'FILE'
DIR = 'DIR'
CMD = 'CMD'


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


def get_lines():
  with open('day7/input.txt', 'r') as f:
    for line in f.readlines():
      yield line.rstrip()


class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.children = []


class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size


class FsBuilder():
  def __init__(self, name):
    self.root = Directory(name)
    self.pwd = self.root

  def cd(self, name):
    if name == '..':
      self.pwd = self.pwd.parent if self.pwd.parent else self.pwd
    else:
      for child in self.pwd.children:
        if isinstance(child, Directory) and child.name == name:
          self.pwd = child

  def createFile(self, name, size):
    f = File(name, size)
    self.pwd.children.append(f)

  def createDir(self, name):
    d = Directory(name, self.pwd)
    self.pwd.children.append(d)


def build_fs(fs, line):
  if line[0] == FILE:
    pass
  elif line[1] == DIR:
    pass
  elif line[2] == CMD:
    pass
  return fs


def part1():
  fs = None
  for line in get_lines():
    if not fs and line[0] == CMD:



def part2():
  pass


def run():
  print('Day 7')
  print(part1())
  print(part2())
