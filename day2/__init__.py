import functools

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
WIN = 'Win'
LOSE = 'Lose'
DRAW = 'Draw'

def get_strategy():
  with open('day2/strategy.txt') as f:
    for line in f:
      play, response = line.strip().split(' ')
      play = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS
      }[play]
      response = {
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS
      }[response]
      yield (play, response)

def winning_shape(shape):
  if shape == ROCK:
    return PAPER
  elif shape == PAPER:
    return SCISSORS
  else: # Scissors
    return ROCK

def losing_shape(shape):
  if shape == ROCK:
    return SCISSORS
  elif shape == PAPER:
    return ROCK
  else: # Scissors
    return PAPER

def round_value(play, response):
  if play == response: # Draw
    return 3
  elif response == winning_shape(play): # Win
    return 6
  else: # Loss
    return 0

def expected_response(condition, value):
  if condition == WIN:
    return winning_shape(value)
  elif condition == LOSE:
    return losing_shape(value)
  else: # Draw
    return value

def shape_value(shape):
  if shape == ROCK:
    return 1
  elif shape == PAPER:
    return 2
  else: # Scissors
    return 3

def part1_results(play, response):
  return shape_value(response) + round_value(play, response)

def part1():
  return functools.reduce(
    lambda score, round : score + part1_results(round[0], round[1]), # Sum score
    get_strategy(), 
    0
  )

def part2_results(play, expected):
  print((play, expected))
  response = { 'X': LOSE, 'Y': DRAW, 'Z': WIN }[expected]
  print((play, response))
  # return part1_results(play, response)

def part2():
  return functools.reduce(
    lambda score, round : score + part2_results(round[0], round[1]), # Sum score
    get_strategy(), 
    0
  )

def run():
  print('Day 2')
  print(part1())
  print(part2())
