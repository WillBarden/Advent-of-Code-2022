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
      yield parse_line(line.rstrip())


class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.children = []

  def get_size(self):
    return sum([child.get_size() for child in self.children])

  def print(self, prefix=''):
    print(prefix + self.name + ' [' + str(self.get_size()) + ']')
    for child in self.children:
      child.print(prefix + ' ') 


class File:
  def __init__(self, name, size):
    self.name = name
    self.size = int(size)

  def get_size(self):
    return self.size

  def print(self, prefix=''):
    print(prefix + self.name + ' [' + str(self.get_size()) + ']')


class FsBuilder():
  def __init__(self, name):
    self.root = Directory(name)
    self.pwd = self.root

  def cd(self, name):
    if name == '..':
      self.pwd = self.pwd.parent if self.pwd.parent else self.pwd
    elif name == '/':
      self.pwd = self.root
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


def dfs(func, fs, agg=None):
  agg = func(agg, fs)
  if isinstance(fs, Directory):
    for child in fs.children:
      agg = dfs(func, child, agg)    
  return agg


def collect(fs, filter=lambda val, agg : True):
  def _collector(agg, val):
    return agg + [val] if filter(val, agg) else agg
  return dfs(_collector, fs, [])


def get_fs():
  builder = None
  for line in get_lines():
    if not builder and line[0] == CMD and line[1][0] == 'cd':
      builder = FsBuilder(line[1][1])
    elif line[0] == CMD and line[1][0] == 'cd':
      builder.cd(line[1][1])
    elif line[0] == FILE:
      builder.createFile(line[2], line[1])
    elif line[0] == DIR:
      builder.createDir(line[1])
  builder.cd('/')
  return builder.root


def part1():
  fs = get_fs()
  return sum([d.get_size() for d in collect(fs, lambda val, agg : isinstance(val, Directory) and val.get_size() <= 100000)])
  

def part2():
  total_space = 70000000
  required_space = 30000000
  fs = get_fs()
  unused_space = total_space - fs.get_size()
  required_removal_space = required_space - unused_space
  def _del_dir(agg, fp):
    if isinstance(fp, Directory):
      if not agg:
        return fp
      elif fp.get_size() >= required_removal_space:
        return agg if agg.get_size() < fp.get_size() else fp
    return agg
  return dfs(_del_dir, fs, None).get_size()


def run():
  print('Day 7')
  print(part1())
  print(part2())
