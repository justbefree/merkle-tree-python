def _derive(values, digestFn):
  if type(values) != list:
    raise TypeError('the first argument must be an array, but ' + str(type(values)) + ' was given')
  if not hasattr(digestFn, '__call__'):
    raise TypeError('the second argument must be a function, but ' + str(type(digestFn)) + ' was given')
  length = len(values)
  results = []
  for i in range(0, length, 2):
    left = values[i]
    right = left if (i + 1 == length) else values[i + 1]
    data = left + right
    results.append(digestFn(data))

  return results

def merkle (values, digestFn):
  if type(values) != list:
    raise TypeError('The first argument must be an array, but ' + str(type(values)) + ' was given')
  if not hasattr(digestFn, '__call__'):
    raise TypeError('The second argument must be a function, but ' + str(type(digestFn)) + ' was given')
  if len(values) == 1:
    return values

  levels = [values]
  level = values
  while len(level) > 1:
    level = _derive(level, digestFn)
    levels.append(level)

  return levels

# def digest(value):
#   return value

# def main():
#   data = merkle([1, 2, 3, 4, 5, 6, 7], digest)
#   print(data)

# if __name__ == '__main__':
#     main()
