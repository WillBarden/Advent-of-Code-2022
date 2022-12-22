def sort(values):
  '''
  Sort the input and return it, as opposed to the in-place sort function.

  :param values: Input values
  :returns: Sorted values
  '''
  values = values.copy()
  values.sort()
  return values


def lcap(values, size):
  '''
  Trim the size of the values list by removing values from the left.

  :param values: Input values
  :param size: Max size of values list
  :returns: Values list with a capped size
  '''
  return values[-size:]


def rcap(values, size):
  '''
  Trim the size of the values list by removing values from the right.

  :param values: Input values
  :param size: Max size of values list
  :returns: Values list with a capped size
  '''
  return values[size:]

