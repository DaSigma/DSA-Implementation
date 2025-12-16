class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value = None):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
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
stack.print_stack()