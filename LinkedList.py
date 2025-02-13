class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
   def __init__(self, value):
      newNode = Node(value)
      self.head = newNode
      self.tail = newNode
      self.length = 1

   def printList(self):
      temp = self.head
      while temp is not None:
         print(temp.value)
         temp = temp.next

   def append(self, value) -> bool:
      newNode = Node(value)
      if self.length == 0:
         self.head = newNode
         self.tail = newNode
      else:
         self.tail.next = newNode
         self.tail = newNode
      self.length += 1
      return True

   def pop(self) -> int:
      if self.length == 0:
         return None
      temp = self.head
      pre = self.head
      while temp.next:
         pre = temp
         temp = temp.next
      self.tail = pre
      self.tail.next = None
      self.length -= 1
      if self.length == 0:
         self.head = None
         self.tail = None
      return temp

   def prepend(self, value) -> bool:
      newNode = Node(value)
      if self.length == 0:
         self.head = newNode
         self.tail = newNode
      else:            
         newNode.next = self.head
         self.head = newNode
      self.length += 1
      return True

   def popFirst(self):
      if self.length == 0:
         return None
      temp = self.head
      self.head = self.head.next
      temp.next = None
      self.length -= 1
      if self.length == 0:
         self.tail = None
      return temp

   def get(self, index):
      if index < 0 or index >= self.length: return None
      temp = self.head
      for _ in range(index):
         temp = temp.next
      return temp

   def setValue(self, index, value) -> bool:
      temp = self.get(index)
      if temp:
         temp.value = value
         return True
      return False

   def insert(self, index, value):
      if index < 0 or index > self.length: return False
      if index == 0:
         self.prepend(value)
      elif index == self.length:
         self.append(value)
      else:         
         newNode = Node(value)
         temp = self.get(index - 1)
         newNode.next = temp.next
         temp.next = newNode
      self.length += 1
      return True

   def remove(self, index) -> Node:
      if index < 0 or index > self.length: return None
      if index == 0:
         self.popFirst()
      if index == self.length - 1:
         self.pop()
      prev = self.get(index - 1)
      temp = prev.next
      prev.next = temp.next
      temp.next = None
      self.length -= 1
      return temp

   def reverse(self):
      # swap head and tail
      curr = self.head
      self.head = self.tail
      self.tail = curr
      
      prev = None
      after = curr.next

      # iterate through the length of the list and reverse the list
      for _ in range(self.length):
         after = curr.next
         curr.next = prev
         prev = curr
         curr = after
      
         
         


my_linked_list = LinkedList(0)

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
# print(my_linked_list.get(3))
# my_linked_list.setValue(3, 9)
# my_linked_list.insert(3, 3)
my_linked_list.reverse()
my_linked_list.printList()
