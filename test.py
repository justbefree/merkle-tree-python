import hashlib
from fastRoot import fastRoot
from index import merkle
from proof import merkleProof, verify

def encropt(value):
  return value

def sha256(value):
  md5 = hashlib.md5()
  md5.update(value.encode(encoding='utf-8'))
  return md5.hexdigest()



def main():
  data = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
  tree = merkle(data, sha256)
  root = fastRoot(data, sha256)
  proof = merkleProof(tree, data[2])
  print(tree)
  print(root)
  print(proof)
  result = verify(proof, sha256)
  print(result)


if __name__ == '__main__':
  main()