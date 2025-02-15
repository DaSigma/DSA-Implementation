import collections


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
                
    def insertRecursive(self, value):
        def insertHelper(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = insertHelper(node.left, value)
            else:
                node.right = insertHelper(node.right, value)
            return node
        self.root = insertHelper(self.root, value)

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

    def BFS(self): #Basic BFS Traversal
        q = collections.deque()
        res = []
        if self.root:
            q.append(self.root)
        while q:
            curr = q.popleft()
            res.append(curr.value)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return res

    def BFSLevels(self):
        q = collections.deque()
        res = []
        if self.root:
            q.append(self.root)
        level = 0
        while q:
            print("Level:", level)
            currLevel = []
            for _ in range(len(q)):
                curr = q.popleft()
                currLevel.append(curr.value)
                print(curr.value)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(currLevel)
            level += 1
        return res

    def dfsPreOrder(self):
        results = []
        def dfs(node):
            if not node: return None
            results.append(node.value)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(self.root)
        return results

    def dfsPostOrder(self):
        results = []
        def dfs(node):
            if not node: return None
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            results.append(node.value)
        dfs(self.root)
        return results
     
    def dfsInOrder(self):
        results = []
        def dfs(node):
            if not node: return None
            if node.left:
                dfs(node.left)
            results.append(node.value)
            if node.right:
                dfs(node.right)
        dfs(self.root)
        return results


tree = BinarySearchTree()
# tree.insert(47)
# tree.insert(21)
# tree.insert(76)
# tree.insert(18)
# tree.insert(27)
# tree.insert(52)
# tree.insert(82)
tree.insertRecursive(47)
tree.insertRecursive(21)
tree.insertRecursive(76)
tree.insertRecursive(18)
tree.insertRecursive(27)
tree.insertRecursive(52)
tree.insertRecursive(82)


# tree = [[47], [21,76], [18,27,52,82]]
# print(tree.BFSLevels())
print(tree.dfsPreOrder())
