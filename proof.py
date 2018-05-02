# caculate the tree node
def treeNodeCount (leafCount):
  count = 1
  i = leafCount
  while i > 1:
    count += i
    i = (i + 1) >> 1

  return count

def treeWidth (n, h):
  return (n + (1 << h) - 1) >> h

def merkleProof (tree, leaf):
  try:
    index = tree.index(leaf)
  except Exception as e:
    # raise RuntimeError(e)
    return None

  n = len(tree)
  nodes = []
  z = treeWidth(n, 1)
  while z > 0:
    if treeNodeCount(z) == n:
      break
    z -= 1

  if z == 0:
    raise RuntimeError('Unknown solution')

  height = 0
  i = 0
  while i < n -1:
    layerWidth = treeWidth(z, height)
    height += 1

    odd = index % 2
    if odd != 0:
      index -= 1

    offset = i + index
    left = tree[offset]
    right = left if index == layerWidth - 1 else tree[offset + 1]

    if i > 0:
      if odd != 0:
        nodes.append(left)
        nodes.append(None)
      else:
        nodes.append(None)
        nodes.append(right)
    else:
      nodes.append(left)
      nodes.append(right)

    index = int(index/2) | 0
    i += layerWidth
  nodes.append(tree[n - 1])
  return nodes


def verify(proof, digestFn):
  if proof == None:
    return False
  root = proof[len(proof) -1]
  hash = root
  for i in range(0, len(proof) -1, 2):
    left = proof[i] or hash
    right = proof[i + 1] or hash
    data = left + right
    hash = digestFn(data)

  return hash == root

