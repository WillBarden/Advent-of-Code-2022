import functools

def get_test_data():
  batch = []
  with open('test_data.txt', 'r') as f:
    for line in (line.strip() for line in f.readlines()):
      if len(line) == 0:
        yield batch
        batch = []
      else:
        batch.append(int(line))


def day1():
  max_sum = functools.reduce(lambda agg, val : max(sum(val), agg), get_test_data(), 0)
  return max_sum


