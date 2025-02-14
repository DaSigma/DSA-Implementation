class Node:
   def __init__(self, value = None):
      self.value = value
      self.next = None

class Queue:
   def __init__(self, value = None):
      newNode = Node(value)
      self.first = newNode
      self.last = newNode
      self.length = 1

   def printQueue(self):
      temp = self.first
      while temp:
         print(temp.value)
         temp = temp.next

   def enqueue(self, value):
      newNode = Node(value)
      if self.length == 0:
         self.first = newNode
         self.last = newNode
      else:
         self.last.next = newNode
         self.last = newNode
      self.length += 1
      return True

   def dequeue(self):
      if self.length == 0:
         return None
      temp = self.first
      if self.length == 1:
         self.first = None
         self.last = None
      else:
         self.first = self.first.next
         temp.next = None
      self.length -= 1
      return temp

q = Queue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.printQueue()