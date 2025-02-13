class Node:
   def __init__(self, value = None):
      self.value = value
      self.left = None
      self.right = None

class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insert(self, value):
      node = Node(value)
      if self.root is None:
         self.root = node
         return True
      temp = self.root
      while True:
         if node.value == temp.value:
            return False
         elif node.value < temp.value:
             if temp.left is None:
                temp.left = node
                return True
             temp = temp.left
         else:
            if temp.right is None:
               temp.right = node
               return True
            temp = temp.right
         
   def contains(self, value):
      temp = self.root
      while temp:
         if value < temp.value:
            temp = temp.left
         elif value > temp.value:
            temp = temp.right
         else:
            return True
      return False

tree = BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(12)

print(tree.contains(2))