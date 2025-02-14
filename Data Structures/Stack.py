class Node:
   def __init__(self, value = None):
      self.value = value
      self.next = None

class Stack:
   def __init__(self, value = None):
      newNode = Node(value)
      self.top = newNode
      self.height = 1

   def printStack(self):
      temp = self.top
      while temp:
         print(temp.value)
         temp = temp.next

   def push(self, value):
      newNode = Node(value)
      if self.height is None:
         self.top = newNode
      else:
         newNode.next = self.top
         self.top = newNode
      self.height += 1
      return True      

   def pop(self):
      if self.top is None:
         return None
      temp =self.top
      self.top = self.top.next
      temp.next = None
      self.height -= 1
      return self.top


stack = Stack('a')
stack.push('b')
stack.push('c')
stack.pop()
stack.printStack()