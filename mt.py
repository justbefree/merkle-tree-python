import os
import hashlib

def get_local_data(path):
      paths = os.listdir(path)
      data = []
      for p in paths:
            fp = open(path+'/'+p)
            data.append(fp.read())
      return data

#print(get_local_data('./doc'))

def add_hash(arr):
      #只处理一个节点的或两个节点的
      hash = hashlib.md5()
      if len(arr) == 1:
            hash.update(bytes(arr[0], encoding='utf-8'))
            return hash.hexdigest()
      elif len(arr) == 2:
            hash.update(bytes(arr[0], encoding='utf-8'))
            hash.update(bytes(arr[1], encoding='utf-8'))
            return hash.hexdigest()
      else:
            print('数据错误...')
            return ''

def data_to_hash(arr):
      result = []
      for i in arr:
            hash = hashlib.md5()
            hash.update(bytes(str(i), encoding='utf-8'))
            result.append(hash.hexdigest())
      return result            

def markel(arr):
      print(arr)
      arr.reverse()
      if len(arr) == 1:
            return arr
      tmp =[]
      result = []
      index = -1
      while(len(arr) > 0):
            index = index + 1
            item = arr.pop()
            if index % 2 == 0:
                  tmp.append(item)
                  if len(arr) == 0:
                        result.append(add_hash(tmp))
                        tmp = []
            else:
                  tmp.append(item)
                  result.append(add_hash(tmp))
                  tmp = []
      
      markel(result)
def main():
      #data = [11,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
      data = get_local_data('./doc')
      hashdata = data_to_hash(data)
      markel(hashdata)

if __name__ == '__main__':
      main()
