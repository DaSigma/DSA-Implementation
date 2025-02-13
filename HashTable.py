class HashTable:
   def __init__(self, size = 7):
      self.dataMap = [None] * size

   def __hash(self, key):
      myHash = 0
      for letter in key:
         myHash = (myHash + ord(letter) * 23) % len(self.dataMap)
         return myHash

   def printTable(self):
      for k, v in enumerate(self.dataMap):
         print(k, ": ", v)

   def setItem(self, key, value):
      index = self.__hash(key)
      if not self.dataMap[index]:
         self.dataMap[index] = []
      self.dataMap[index].append([key, value])

   def getItem(self, key):
      index = self.__hash(key)
      if self.dataMap[index]:
         for i in range(len(self.dataMap[index])):
            if self.dataMap[index][i][0] == key:
               return self.dataMap[index][i][1]
      return None

   def getKeys(self):
      allKeys = []
      for i in range(len(self.dataMap)):
         if self.dataMap[i]:
            for j in range(len(self.dataMap[i])):
               allKeys.append(self.dataMap[i][j][0])
      return allKeys

ht = HashTable()
ht.setItem('bike', 25)
ht.setItem('bolts', 685)
ht.setItem('lumber', 296)
print(ht.getKeys())
ht.printTable()