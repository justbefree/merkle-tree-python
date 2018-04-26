from fastRoot import fastRoot
from index import merkle

def encropt(value):
  return value


def main():
  root = fastRoot([1, 2, 3, 4, 5, 6, 7], encropt)
  data = merkle([1, 2, 3, 4, 5, 6, 7], encropt)
  print(root)
  print(data)

if __name__ == '__main__':
  main()