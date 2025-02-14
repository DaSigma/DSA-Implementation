class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
   def __init__(self, value):
      newNode = Node(value)
      self.head = newNode
      self.tail = newNode
      self.length = 1

   def printList(self):
      curr = self.head
      while curr:
         print(curr.value)
         curr = curr.next

   def append(self, value):
      newNode = Node(value)
      if self.head is None:
         self.head = newNode
         self.tail = newNode
      else:
         self.tail.next = newNode
         newNode.prev = self.tail
         self.tail = newNode
      self.length += 1
      return True

   def pop(self):
      if self.length == 0:
         return None
      temp = self.tail
      if self.length == 1:
         self.tail = None
         self.head = None
      else:
         self.tail = self.tail.prev
         self.tail.next = None
         temp.prev = None
      self.length -= 1
      return temp

   def prepend(self, value):
      newNode = Node(value)
      if self.head is None:
         self.head = newNode
         self.tail = newNode
      else:
         newNode.next = self.head
         self.head.prev = newNode
         self.head = newNode
      self.length += 1
      return True

   def popFirst(self):
      if self.head == 0:
         return None
      temp = self.head
      if self.length == 1:
         self.head = None
         self.tail = None
      else:
         self.head = self.head.next
         self.head.prev = None
         temp.next = None
      self.length -= 1
      return temp

   def get(self, index):
      if index < 0 or index >= self.length:
         return None
      temp = self.head
      if index < self.length / 2:
         for _ in range(index):
               temp = temp.next
      else:
         temp = self.tail
         for _ in range(self.length - 1, index, -1):
               temp = temp.prev
      return temp

   def setValue(self, index, value):
      temp = self.get(index)
      if temp:
         temp.value = value
         return True
      return False

   def insert(self, index, value):
      if index < 0 or index > self.length:
         return False
      if index == 0:
         self.prepend(value)
      elif index == self.length:
         self.append(value)
      else:
         newNode = Node(value)
         before = self.get(index - 1)
         after = before.next
         newNode.prev = before
         newNode.next = after
         before.next = newNode
         after.prev = newNode
      self.length += 1
      return True

   def remove(self, index):
      if index < 0 or index > self.length:
         return None
      if index == 0:
         return self.popFirst()
      elif index == self.length - 1:
         return self.pop()
      else:
         temp = self.get(index)
         temp.next.prev = temp.prev
         temp.prev.next = temp.next
         temp.next = None
         temp.prev = None
      self.length -= 1
      return temp     


newDL = DoublyLinkedList(1)
newDL.append(2)
newDL.append(3)
newDL.append(5)
newDL.prepend(0)
newDL.remove(4)
newDL.printList()
