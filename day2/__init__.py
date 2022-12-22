from functools import reduce


ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
WIN = 'Win'
LOSS = 'Lose'
DRAW = 'Draw'
ORDER = [ROCK, PAPER, SCISSORS]


def get_strategy():
  with open('day2/strategy.txt') as f:
    for line in f:
      first, second = line.strip().split(' ')
      yield (first, second)


def winning_shape(shape):
  '''
  Get the shape that beats the specified shape
  '''
  return ORDER[(ORDER.index(shape) + 1) % len(ORDER)]


def losing_shape(shape):
  '''
  Get the shape that loses to the specified shape
  '''
  return ORDER[(ORDER.index(shape) - 1) % len(ORDER)]


def shape_value(shape):
  '''
  Return the value score of the shape
  '''
  return { ROCK: 1, PAPER: 2, SCISSORS: 3 }[shape]


def outcome(first_shape, second_shape):
  '''
  Get the outcome value based on the shape matchups
  '''
  if winning_shape(first_shape) == second_shape:
    return WIN
  elif first_shape == winning_shape(second_shape):
    return LOSS
  elif first_shape == second_shape:
    return DRAW


def outcome_value(outcome):
  '''
  Return the score for the specified outcome
  '''
  return { WIN: 6, DRAW: 3, LOSS: 0 }[outcome]


def expected_second_shape(first_shape, outcome):
  '''
  Get the second symbol required for the desired outcome
  '''
  if outcome == WIN:
    return winning_shape(first_shape)
  elif outcome == LOSS:
    return losing_shape(first_shape)
  else:
    return first_shape


def expected_outcome(symbol):
  '''
  Return the expected outcome based on the symbol
  '''
  return { 'X': LOSS, 'Y': DRAW, 'Z': WIN }[symbol]


def first_shape(shape):
  '''
  Return the shape based on the first symbol
  '''
  return { 'A': ROCK, 'B': PAPER, 'C': SCISSORS }[shape]


def second_shape(shape):
  '''
  Return the shape based on the second symbol
  '''
  return { 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS }[shape]


def part1():
  def result(first_symbol, second_symbol):
    shapes = (first_shape(first_symbol), second_shape(second_symbol))
    return outcome_value(outcome(shapes[0], shapes[1])) + shape_value(shapes[1])
  return reduce(lambda score, round : score + result(round[0], round[1]), get_strategy(), 0)


def part2():
  def result(first_symbol, second_symbol):
    exp_outcome = expected_outcome(second_symbol)
    return outcome_value(exp_outcome) + shape_value(expected_second_shape(first_shape(first_symbol), exp_outcome))
  return reduce(lambda score, round : score + result(round[0], round[1]), get_strategy(), 0)


def run():
  print('Day 2')
  print(part1())
  print(part2())
