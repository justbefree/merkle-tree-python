def fastRoot(values, digestFn):
  if type(values) != list:
    raise TypeError('The first argument must be an array, but ' + str(type(values)) + ' was given !')
  if not hasattr(digestFn, '__call__'):
    raise TypeError('The second argument must be a function, but ' + str(type(digestFn)) + ' was given !')
  length = len(values)
  results = []
  results.extend(values)
  while length > 1:
    j = 0
    for i in range(0, length, 2):
      left = results[i]
      right = left if (i + 1 == length) else results[i + 1]
      data = left + right #bytes(str(left) + str(right), encoding='utf-8')
      results[j] = digestFn(data)
      j += 1
    length = j
  return results[0]

# def encropt(value):
#   return value

# def main():
#   root = fastRoot([1, 2, 3, 4, 5, 6, 7], encropt)
#   print(root)

# if __name__ == '__main__':
#   main()